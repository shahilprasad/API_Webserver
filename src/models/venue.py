from init import db, ma
from marshmallow import fields

class Venue(db.Model):
    __tablename__= "venues"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    suburb = db.Column(db.String())
    postcode= db.Column(db.Integer())

class VenueSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'address', 'suburb', 'postcode')