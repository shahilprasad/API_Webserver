from init import db

class Venue(db.Model):
    __tablename__= "venues"

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String())
    address = db.Column(db.String())
    suburb = db.Column(db.String())
    postcode= db.Column(db.Integer())
