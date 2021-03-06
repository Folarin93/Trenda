from main import db


class Lang_watchlist(db.Model):
    __tablename__="lang_watchlist"
    lang_watchlist_id = db.Column(db.Integer,primary_key=True)
    language_id = db.Column(db.Integer, db.ForeignKey("languages.id"), nullable=False)
    watchlist_id = db.Column(db.Integer, db.ForeignKey("watchlist.id"), nullable=False)




