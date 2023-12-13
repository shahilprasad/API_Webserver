from flask import Blueprint, request
from init import db, bcrypt
from models.user import User, UserSchema
from sqlalchemy.exc import IntegrityError

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
    try:
        # Load and validate the request data
        user_info = UserSchema(only=['username', 'password']).load(request.json)

        # Query the database for a user with the given username
        user = User.query.filter_by(username=user_info['username']).first()

        # If the user exists and the password matches, return the user
        if user and bcrypt.check_password_hash(user.password, user_info['password']):
            return UserSchema(exclude=['password', 'is_admin', 'id']).dump(user)
        
        # Otherwise, return an error message
        else:
            return {'error': 'Invalid username or password'}, 401
    except KeyError:
        return {'error': 'Invalid request'}, 400
    
# Allows admin to get a list of all users
@users_bp.route('/', methods=['GET'])
def get_users():
    stmt = db.select(User)
    users = db.session.scalars(stmt).all()
    return UserSchema(many=True).dump(users)