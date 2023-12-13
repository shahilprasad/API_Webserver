from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt

# Creatiing db object 
db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()
