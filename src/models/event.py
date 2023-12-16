from init import db, ma
from marshmallow import fields
from datetime import date, time
from marshmallow.validate import Length


class Event(db.Model):
    __tablename__= "events"
   
    id = db.Column(db.Integer,primary_key=True)
    event_name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    start_time = db.Column(db.Time, nullable=False)
    end_time = db.Column(db.Time, nullable=False)

    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    venue = db.relationship('Venue')

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='events')

class EventSchema(ma.Schema):
    venue = fields.Nested('VenueSchema', only=['id', 'name'])
    user = fields.Nested('UserSchema', only=['id', 'username'])
    # Validation
    event_name = fields.String(required=True, validate=Length(min=1, error='Event name must not be empty'))
    description = fields.String(required=True, validate=Length(min=1, error='Description must not be empty'))

    class Meta:
        fields = ('id', 'event_name', 'description', 'date', 'start_time', 'end_time', 'venue', 'user')
