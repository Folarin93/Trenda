# from main import mar
# from models.Lang_watchlist import Lang_watchlist
# from schemas.LanguageSchema import languages_schema
# from schemas.WatchlistSchema import watchlists_schema


# class Lang_watchlistSchema(mar.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Lang_watchlist
#         # include_fk = True
#     languages = mar.Nested(languages_schema)
#     watchlists = mar.Nested(watchlists_schema)

# lang_watchlist_schema = Lang_watchlistSchema()
# lang_watchlists_schema = Lang_watchlistSchema(many=True)