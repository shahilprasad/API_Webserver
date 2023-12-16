from init import db, ma
from datetime import datetime
from marshmallow import fields, validate

class Queue(db.Model):
    __tablename__= "queues"

    id = db.Column(db.Integer,primary_key=True)
    wait_time = db.Column(db.String, nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.now().strftime("%Y-%m-%d %H:%M"))
    comment = db.Column(db.String())

    venue_id = db.Column(db.Integer, db.ForeignKey('venues.id'))
    venue = db.relationship('Venue', back_populates='queue')

class QueueSchema(ma.Schema):
    venue = fields.Nested('VenueSchema', exclude=['queue'])
    user = fields.Nested('UserSchema', only=['id'])
    # Validation
    wait_time = fields.String(required=True, validate=validate.Length(min=1, error='Wait time must not be empty'))
    comment = fields.String(validate=validate.Length(max=200, error='Comment must be less than 200 characters'))

    class Meta:
        fields = ('id', 'wait_time', 'last_updated', 'comment', 'venue', 'user')
