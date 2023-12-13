from flask import Blueprint, request
from init import db
from models.venue import Venue, VenueSchema
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from auth import admin_only

venues_bp = Blueprint('venues', __name__, url_prefix='/venues')

# Define a route for getting a list of all venues
@venues_bp.route("/", methods=['GET'])
def all_venues():
    stmt = db.select(Venue)
    venues = db.session.scalars(stmt).all()
    return VenueSchema(many=True).dump(venues)

# Define a route for getting a single venue
@venues_bp.route("/<int:id>", methods=['GET'])
def get_venue(id):
    stmt = db.select(Venue).where(Venue.id == id)
    venue = db.session.scalar(stmt)

    # Return the venue if it exists
    if venue:
        return VenueSchema().dump(venue)
    # Return error message if venue does not exist
    else:
        return {'error':'Venue not found'}, 404

# Define a route for creating a new venue
@venues_bp.route("/", methods=['POST'])
@jwt_required()
def create_venue():
    # Load and validate the request data
    venue_info = VenueSchema(exclude=['id']).load(request.json)
    # Create a new venue object
    venue = Venue(
        name = venue_info['name'],
        address = venue_info['address'],
        suburb = venue_info['suburb'],
        postcode = venue_info['postcode']
    )
    # Add the new venue to the database
    db.session.add(venue)
    db.session.commit()

    # Serialize new Venue instance to JSON, and return serialized Venue
    return VenueSchema().dump(venue), 201
    
# Allows admin to delete a venue
@venues_bp.route("/<int:id>", methods=['DELETE'])
@jwt_required()
def delete_venue(id):
    admin_only()
    # Query the database for a venue with the given id
    stmt = db.select(Venue).filter_by(id=id)
    venue = db.session.scalar(stmt)

    # Delete the venue from the database
    if venue:
        db.session.delete(venue)
        db.session.commit()
        # Return empty list if successful
        return {}, 200
    # Return error message if venue does not exist
    else:
        return {'error':'Venue not found'}, 404
