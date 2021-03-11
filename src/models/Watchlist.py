from main import db
# from models.Lang_watchlist import Lang_watchlist

class Watchlist(db.Model):
    __tablename__="watchlist"
    id = db.Column(db.Integer,primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    language_id = db.Column(db.Integer, db.ForeignKey("languages.id"), nullable=False)

    # lang_watchlist = db.relationship("Lang_watchlist", backref="watchlist")
    