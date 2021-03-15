from main import db
from models.Watchlist import Watchlist


class Languages(db.Model):
    __tablename__="languages"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    details = db.Column(db.JSON())
    watchlist = db.relationship("Watchlist", backref="language")
