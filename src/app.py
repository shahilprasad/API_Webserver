from flask import Flask
from os import environ
from init import *
from blueprints.cli_bp import db_cmd
from blueprints.venues_bp import venues_bp
from blueprints.users_bp import users_bp
from blueprints.events_bp import events_bp
from sqlalchemy.exc import DataError, IntegrityError
from marshmallow.exceptions import ValidationError

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

    # Error handling which returns JSON error messages
    @app.errorhandler(401)
    def unauthorized(err):
        return {'error': str(err)}, 401
  
    @app.errorhandler(404)
    def not_found(err):
        return {'error': str(err)}, 404
    
    @app.errorhandler(405)
    def method_not_allowed(err):
        return {'error': str(err)}, 405
    
    @app.errorhandler(422)
    def unprocessable_entity(err):
        return {'error': str(err)}, 422
    
    @app.errorhandler(500)
    def internal_server_error(err):
        return {'error': str(err)}, 500
    
    @app.errorhandler(ValidationError)
    def validation_error(err):
        return {'error': str(err)}, 400
    
    @app.errorhandler(DataError)
    def data_error(err):
        return {'error': str(err)}, 400

    @app.errorhandler(IntegrityError)
    def integrity_error(err):
        return {'error': str(err)}, 409

    @app.errorhandler(400)
    def bad_request(err):
        return {'error': str(err)}, 400
    
    @app.errorhandler(KeyError)
    def keyerror(err):
        missing_field = err
        error_message = f"Missing fields required: {(missing_field)}"
        return {'error': error_message}, 400
    
    # Register blueprints
    app.register_blueprint(db_cmd)
    app.register_blueprint(venues_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(events_bp)

    return app