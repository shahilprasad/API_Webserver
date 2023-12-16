from flask import Blueprint, request
from init import db
from models.queue import Queue, QueueSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from auth import authorization

queues_bp = Blueprint('queues', __name__, url_prefix='<int:venue_id>/queue')

# Create a queue info status
@queues_bp.route("/", methods=['POST'])
@jwt_required()
def create_queue(venue_id):
    # Load and validate the request data
    queue_info = QueueSchema(exclude=['id']).load(request.json)
    # Create a new queue object
    queue = Queue(
        venue_id = venue_id,  
        wait_time = queue_info['wait_time'],
        # last_updated = queue_info['last_updated'],
        comment = queue_info['comment']
    )
    # Add the new queue info to the database
    db.session.add(queue)
    db.session.commit()

    # Serialize new Queue instance to JSON, and return serialized Queue
    return QueueSchema(exclude=['user']).dump(queue), 201

# Get queue info for a venue
@queues_bp.route("/", methods=['GET'])
def get_queue(venue_id):
    stmt = db.select(Queue).where(Queue.venue_id == venue_id)
    queue = db.session.scalar(stmt)

    # Return the queue if it exists
    if queue:
        return QueueSchema().dump(queue)
    # Return error message if queue does not exist
    else:
        return {'error':'Queue not found'}, 404
    
# Allows admin or user who created venue to delete queue info
@queues_bp.route("/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_queue(id, venue_id):
    # Query the database for a queue with the given venue_id
    stmt = db.select(Queue).filter_by(id=id)
    queue = db.session.scalar(stmt)

    # If queue exists, delete it
    if queue:
        authorization(queue.venue_id)
        db.session.delete(queue)
        db.session.commit()
        return {}, 200
    # Otherwise, return error message
    else:
        return {'error': 'Queue not found'}, 404