from main import db
from models.Watchlist import Watchlist
from flask_login import UserMixin

def get_user(user_id):
    user=Users.query.filter_by(id=user_id).first()
    return user

class Users(db.Model, UserMixin):
    __tablename__="users"
    id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    username = db.Column(db.String(), unique=True, nullable=False)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.Integer())
    watchlist = db.relationship("Watchlist", backref="user", cascade="all, delete")

