from main import db
from models.Watchlist import Watchlist

class Users(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=True, nullable=False)
    phone = db.Column(db.Integer())
    watchlist = db.relationship("Watchlist", backref="user")