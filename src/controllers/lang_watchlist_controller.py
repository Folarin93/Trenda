from main import db
from models.Lang_watchlist import Lang_watchlist
from schemas.Lang_watchlistSchema import lang_watchlist_schema, lang_watchlists_schema
from flask import Blueprint, request, jsonify

lang_watchlists = Blueprint('lang_watchlists', __name__, url_prefix="/lang_watchlists")

@lang_watchlists.route("/", methods=["GET"])
def lang_watchlists_index():
    lang_watchlists = Lang_watchlist.query.all()
    return jsonify(lang_watchlist_schema.dump(lang_watchlists))