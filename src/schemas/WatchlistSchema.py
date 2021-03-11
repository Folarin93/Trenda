from main import mar
from models.Watchlist import Watchlist
from schemas.UserSchema import user_schema
from schemas.LanguageSchema import language_schema
# from models.User import Users

class WatchlistSchema(mar.SQLAlchemyAutoSchema):
    class Meta:
        model = Watchlist
        # include_fk = True
    
    user = mar.Nested(user_schema)
    language = mar.Nested(language_schema)

watchlist_schema = WatchlistSchema()
watchlists_schema = WatchlistSchema(many=True)
