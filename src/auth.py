from flask_jwt_extended import get_jwt_identity
from models.user import User
from init import db
from flask import abort

# Create a function for admin only functions
def admin_only():
    # Retrieve susername from token
    user_id = get_jwt_identity()
    # Query the database for a user with the given username
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    # If user is not an admin, abort
    if not user.is_admin:
        abort(401)