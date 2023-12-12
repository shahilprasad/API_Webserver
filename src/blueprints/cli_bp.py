from flask import Blueprint
from app import db
from models.user import User
from models.venue import Venue
from models.event import Event
from models.queue import Queue


# Setuo the blueprint for db commands
db_cmd = Blueprint("db", __name__)

# Reset tables in the database
@db_cmd.cli.command("create")
def create_db():
    # Drop all exisiting tables
    db.drop_all()
    # Create new tables with 
    db.create_all()
    print("Tables created")

@db_cmd.cli.command("seed")
def seed_db():
    users = [
        User(
            username = "admin",
            email = 'admin@foo.com',
            password = 'dizzyjungle',
            is_admin = True
        ),
        User(
            username = 'Patron',
            email = 'patron@foo.com',
            password = 'waterpark'
        )
    ]

    db.session.add_all(users)
    db.session.commit()

    venues = [
        Venue(
            name = "The Underground",
            address = "13 Main Street",
            suburb = "Narnia",
            postcode = "2929"
        ),
        Venue(
            name = "The Underground",
            address = "13 Main Street",
            suburb = "Narnia",
            postcode = "2929"
        )
    ]

    db.session.add_all(venues)
    db.session.commit()

    events = [
        Event(
            event_name = "Funk Town",
            description = "An old school disco vibe, with multiple DJ's playing classics from the 80's",
            date = "2023-12-01",
            start_time = "12:00",
            end_time = "20:00",
        ),
        Event(
            event_name = "Boiler House",
            description = "Get your techno on with a night of hard hitting beats, with house, techno and dnb acts",
            date = "2023-12-02",
            start_time = "14:00",
            end_time = "23:00",
        )
    ]

    db.session.add_all(events)
    db.session.commit()

    queues = [
        Queue(
            status = "Busy",
            wait_time = "5 Minutes",
            last_updated = "18:30",
            comment = "Line is moving moderately fast"
        ),
        Queue(
            status = "Busy",
            wait_time = "25 Minutes",
            last_updated = "16:30",
            comment = "Line is moving slowly, long wait due to extra security measures"
        )
    ]

    db.session.add_all(queues)
    db.session.commit()

    print("Database seeded")