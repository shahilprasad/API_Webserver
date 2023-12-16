from init import db, ma
from marshmallow import fields, validate

class Venue(db.Model):
    __tablename__= "venues"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    address = db.Column(db.String, nullable=False)
    suburb = db.Column(db.String, nullable=False)
    postcode= db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='venues')

    queue = db.relationship('Queue', back_populates='venue')
    event = db.relationship('Event', back_populates='venue')

class VenueSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'username'])
    queue = fields.Nested('QueueSchema', many=True, exclude=['venue', 'user'])
    event = fields.Nested('EventSchema', many=True, exclude=['venue', 'user'])
    # Validation
    name = fields.String(required=True)

    class Meta:
        fields = ('id', 'name', 'address', 'suburb', 'postcode', 'event', 'queue', 'user')