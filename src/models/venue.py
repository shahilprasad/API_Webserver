from init import db, ma
from marshmallow import fields

class Venue(db.Model):
    __tablename__= "venues"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    suburb = db.Column(db.String())
    postcode= db.Column(db.Integer())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='venues')

    queue = db.relationship('Queue', back_populates='venue')
    event = db.relationship('Event', back_populates='venue')

class VenueSchema(ma.Schema):
    user = fields.Nested('UserSchema', only=['id', 'username'])
    queue = fields.Nested('QueueSchema')

    class Meta:
        fields = ('id', 'name', 'address', 'suburb', 'postcode', 'user', 'queue')