from flask import Blueprint, request
from init import db
from models.queue import Queue, QueueSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from auth import admin_only

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
        last_updated = queue_info['last_updated'],
        comment = queue_info['comment']
    )
    # Add the new queue info to the database
    db.session.add(queue)
    db.session.commit()

    # Serialize new Queue instance to JSON, and return serialized Queue
    return QueueSchema(exclude=['user']).dump(queue), 201