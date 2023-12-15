from init import db, ma
from datetime import datetime
from marshmallow import fields

class Queue(db.Model):
    __tablename__= "queues"

    id = db.Column(db.Integer,primary_key=True)
    wait_time = db.Column(db.String())
    last_updated = db.Column(db.Date, default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    comment = db.Column(db.String())

    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    venue = db.relationship('Venue', back_populates='queue')

class QueueSchema(ma.Schema):
    venue = fields.Nested('VenueSchema')
    user = fields.Nested('UserSchema', only=['id'])

    class Meta:
        fields = ('id', 'wait_time', 'last_updated', 'comment', 'venue', 'user')
