from main import db
from models.Lang_watchlist import Lang_watchlist

class Languages(db.Model):
    __tablename__="languages"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(), unique=True, nullable=False)
    details = db.Column(db.JSON())
    lang_watchlist = db.relationship("Lang_watchlist", backref="languages")