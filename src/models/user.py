from init import db, ma
from marshmallow import fields, validate
from marshmallow.validate import Length

class User(db.Model):
    __tablename__= "users"
   
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

    venues = db.relationship('Venue', back_populates='user')
    events = db.relationship('Event', back_populates='user')

class UserSchema(ma.Schema):
    venues = fields.Nested('VenueSchema', many=True, only=['id', 'name'])
    # Validation
    email = fields.Email(required=True)
    password = fields.String(required=True, validate=Length(min=6, error='Password must be a minimum of 6 characters'))
    username = fields.String(required=True, validate=Length(min=1, error='Username must not be empty'))

    class Meta:
        fields = ('id', 'username', 'email', 'password', 'is_admin', 'venues')