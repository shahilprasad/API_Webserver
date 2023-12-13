from flask import Flask
from os import environ
from init import *
from blueprints.cli_bp import db_cmd
from blueprints.venues_bp import venues_bp
from blueprints.users_bp import users_bp

def create_app():
    # Initialize app by creating flask app object
    app = Flask(__name__)
    
    # Obtains secured JWT_KEY and DATABASE_URI connection values from .env
    app.config['JWT_SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

    # Initialized object from init file for use 
    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Error handling whic returns JSON error messages
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401

    app.register_blueprint(db_cmd)
    app.register_blueprint(venues_bp)
    app.register_blueprint(users_bp)

    return app