from main import db
from models.User import Users
from schemas.UserSchema import user_schema, users_schema
from models.Watchlist import Watchlist
from schemas.WatchlistSchema import watchlist_schema, watchlists_schema
from models.Language import Languages
from schemas.LanguageSchema import language_schema, languages_schema
from models.Lang_watchlist import Lang_watchlist
from schemas.Lang_watchlistSchema import lang_watchlist_schema, lang_watchlists_schema
from flask import Blueprint, request, jsonify, render_template

users = Blueprint('users', __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def user_index():
    users = Users.query.all()
    return render_template("users_index.html", my_users = users)
    # return jsonify(users_schema.dump(users))


@users.route("/<int:id>", methods=["GET"])
def user_show(id):
    users = Users.query.get(id)
    return render_template("user_show.html", my_user = users)
    # return jsonify(user_schema.dump(users))

@users.route("/<int:id>/watchlists", methods=["GET"])
def user_watchlists_show(id):
    user_watchlists = Watchlist.query.filter_by(user_id=id)
    return render_template("user_watchlist.html", my_user_watchlists = user_watchlists)
    # return jsonify(watchlists_schema.dump(user_watchlists))

    
    # user_watchlist_lang_watchlist = Lang_watchlist.query.filter_by(lang_watchlist=user_watchlists.id)
    # user_watchlist_languages = Languages.query.filter_by(lang_watchlist=user_watchlist_lang_watchlist.language_id)
    # return render_template("user_watchlist.html", my_user_watchlists = user_watchlists.lang_watchlist, my_user_watchlist_languages = my_user_watchlist_languages)
