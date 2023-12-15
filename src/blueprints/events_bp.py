from flask import Blueprint, request
from init import db
from models.event import Event, EventSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from auth import admin_only

events_bp = Blueprint('events', __name__, url_prefix='/<int:venue_id>/events')

# Define a route for getting a list of all events
@events_bp.route("/", methods=['GET'])
def all_events(venue_id):
    stmt = db.select(Event)
    events = db.session.scalars(stmt).all()
    return EventSchema(many=True).dump(events)

# Define a route for getting a single event
@events_bp.route("/<int:id>", methods=['GET'])
def get_event(id):
    stmt = db.select(Event).where(Event.id == id)
    event = db.session.scalar(stmt)

    # Return the event if it exists
    if event:
        return EventSchema().dump(event)
    # Return error message if event does not exist
    else:
        return {'error':'Event not found'}, 404