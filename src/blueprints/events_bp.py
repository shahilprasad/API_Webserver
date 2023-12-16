from flask import Blueprint, request
from init import db
from models.event import Event, EventSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from auth import authorization

events_bp = Blueprint('events', __name__, url_prefix='/<int:venue_id>/events')

# Define a route for getting a list of all events at a venue
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
    
# Define a route for creating a new event for a venue
@events_bp.route("/", methods=['POST'])
@jwt_required()
def create_event(venue_id):
    # Load and validate the request data
    event_info = EventSchema(exclude=['id']).load(request.json)
    # Create a new event object
    event = Event(
        venue_id = venue_id,  
        event_name = event_info['event_name'],
        description = event_info['description'],
        date = event_info['date'],
        start_time = event_info['start_time'],
        end_time = event_info['end_time'],
        user_id = get_jwt_identity()
    )
    # Add the new event to the database
    db.session.add(event)
    db.session.commit()

    # Serialize new Event instance to JSON, and return serialized Event
    return EventSchema(exclude=['venue']).dump(event), 201

# Updating an event (either admin or user that created the event)
@events_bp.route("/<int:id>", methods=['PUT', 'PATCH'])
@jwt_required()
def update_event(id):
    # Load and validate the request data
    event_info = EventSchema(exclude=['id']).load(request.json)
    # Query the database for an event with the given id
    stmt = db.select(Event).where(Event.id == id)
    event = db.session.scalar(stmt)

    # If the event exists, update it
    if event:
        authorization(event.user_id)
        # Update the event with the new info
        event.event_name = event_info.get('event_name', event.event_name)
        event.description = event_info.get('description', event.description)
        event.date = event_info.get('date', event.date)
        event.start_time = event_info.get('start_time', event.start_time)
        event.end_time = event_info.get('end_time', event.end_time)
        # Commit the changes to the database
        db.session.commit()
        # Return the updated event
        return EventSchema(exclude=['venue']).dump(event)
    # Return error message if event does not exist
    else:
        return {'error':'Event not found'}, 404
    
# Delete the event (either admin or user that created the event)
@events_bp.route("/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_event(id, venue_id):
    # Query the database for an event with the given id
    stmt = db.select(Event).filter_by(id=id)
    event = db.session.scalar(stmt)

    # If the event exists, delete it
    if event:
        authorization(event.user_id)
        db.session.delete(event)
        db.session.commit()
        # Return empty list to confirm deletion
        return {}, 200
    # Return error message if event does not exist
    else:
        return {'error':'Event not found'}, 404