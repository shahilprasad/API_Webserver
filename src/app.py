from flask import Flask
from os import environ
from init import *

def create_app():
    # Initialize app by creating flask app object
    app = Flask(__name__)
    
    # Obtains secured JWT_KEY and DATABASE_URI connection values from .env
    app.config['JWT_SECRET_KEY'] = environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL')

    # Initialized object from init file for use
    db.init_app(app)

    return app