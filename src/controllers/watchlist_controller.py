from main import db
from models.Watchlist import Watchlist
from schemas.WatchlistSchema import watchlist_schema, watchlists_schema
from flask import Blueprint, request, jsonify, render_template

watchlists = Blueprint('watchlists', __name__, url_prefix="/watchlists")

@watchlists.route("/", methods=["GET"])
def watchlist_index():
    watchlists = Watchlist.query.all()
    return render_template("watchlists_index.html", watchlists = watchlists)
    # return jsonify(watchlists_schema.dump(watchlists))