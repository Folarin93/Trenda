from main import db
from models.Watchlist import Watchlist
from schemas.WatchlistSchema import watchlist_schema, watchlists_schema
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required

watchlists = Blueprint('watchlists', __name__, url_prefix="/watchlists")

@watchlists.route("/delete/<int:id>", methods=["GET"])
@login_required
def watchlist_delete(id):
    watchlist = Watchlist.query.get(id)
    
    db.session.delete(watchlist)
    db.session.commit()

    return redirect(url_for('users.user_languages', id=current_user.id))

@watchlists.route("/create/<int:id>/<int:lang_id>", methods=["GET"])
@login_required
def watchlist_create(id, lang_id):
    watchlist = Watchlist()
    watchlist.user_id = id
    watchlist.language_id = lang_id
    

    db.session.add(watchlist)
    db.session.commit()

    return redirect(url_for('users.user_languages', id=current_user.id))

# @watchlists.route("/", methods=["GET"])
# def watchlist_index():
#     watchlists = Watchlist.query.all()
#     return jsonify(watchlists_schema.dump(watchlists))