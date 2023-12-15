from init import db, ma
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field

class Event(db.Model):
    __tablename__= "events"
   
    id = db.Column(db.Integer,primary_key=True)
    event_name = db.Column(db.String())
    description = db.Column(db.String())
    date = db.Column(db.Date())
    start_time = db.Column(db.Time())
    end_time = db.Column(db.Time())

    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    venue = db.relationship('Venue')

class EventSchema(ma.Schema):
    venue = fields.Nested('VenueSchema')

    class Meta:
        fields = ('id', 'event_name', 'description', 'date', 'start_time', 'end_time', 'venue')