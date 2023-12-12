from init import db

class Event(db.Model):
    __tablename__= "events"
   
    id = db.Column(db.Integer,primary_key=True)
    event_name = db.Column(db.String())
    description = db.Column(db.String())
    date = db.Column(db.Date())
    start_time = db.Column(db.Time())
    end_time = db.Column(db.Time())