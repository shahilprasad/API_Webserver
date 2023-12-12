from init import db

class Queue(db.Model):
    __tablename__= "queues"

    id = db.Column(db.Integer,primary_key=True)
    status = db.Column(db.String())
    wait_time = db.Column(db.String())
    last_updated = db.Column(db.Time())
    comment = db.Column(db.String())