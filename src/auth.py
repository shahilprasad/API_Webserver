from flask_jwt_extended import get_jwt_identity
from models.user import User
from init import db
from flask import abort

# Create a function for admin or user only functions
def authorization(user_id=None):
    # Retrieve susername from token
    jwt_user_id = get_jwt_identity()
    # Query the database for a user with the given username
    stmt = db.select(User).filter_by(id=jwt_user_id)
    user = db.session.scalar(stmt)
    # If user is not an admin, or the user that created the resource, abort
    if not (user.is_admin or (user_id and jwt_user_id == user_id)):
        abort(401, description="You are not authorized to perform this action")