from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta
from auth import admin_only

users_bp = Blueprint('users', __name__, url_prefix='/users')

# Allows a new user to register
@users_bp.route('/register', methods=['POST'])
def register():
    try:
        # Load and validate the request data
        user_info = UserSchema(exclude=['id']).load(request.json)
        # Create a new user object
        user = User(
            username = user_info['username'],
            email = user_info['email'],
            password = bcrypt.generate_password_hash(user_info['password']).decode('utf8')
        )
        # Add the new user to the database
        db.session.add(user)
        db.session.commit()

        # Serialize new User instance to JSON, and return serialized User
        return UserSchema(exclude=['password', 'is_admin']).dump(user), 201
    
    # Return error message if username is already taken
    except IntegrityError:
        return {'error': 'Username already exists'}, 409

# Allows a user to login
@users_bp.route('/login', methods=['POST'])
def login():
    # Load and validate the request data
    user_info = UserSchema(only=['username', 'password']).load(request.json)

    # Query the database for a user with the given username
    stmt = db.select(User).where(User.username == user_info['username'])
    user = db.session.scalar(stmt)

    # If the user exists and the password matches, return the user
    if user and bcrypt.check_password_hash(user.password, user_info['password']):
        # Create a JWT token for the user
        token = create_access_token(identity=user.id, expires_delta=timedelta(hours=2))
        # Return the user and JWT token
        return {'token': token, 'user': UserSchema(exclude=['password', 'is_admin', 'id', 'venues']).dump(user)}
        
        # Otherwise, return an error message
    else:
        return {'error': 'Invalid username or password'}, 401
   
    
# Allows admin to get a list of all users
@users_bp.route('/', methods=['GET'])
@jwt_required()
def get_users():
    admin_only()
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(exclude=['password'], many=True).dump(users)