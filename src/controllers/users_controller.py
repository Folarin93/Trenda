from main import db
from models.User import Users
from schemas.UserSchema import user_schema, users_schema
from models.Watchlist import Watchlist
from schemas.WatchlistSchema import watchlist_schema, watchlists_schema
from models.Language import Languages
from schemas.LanguageSchema import language_schema, languages_schema
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for
from flask_login import login_user, current_user, logout_user, login_required
from flask_jwt_extended import jwt_required

users = Blueprint('users', __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def user_index():
    users = Users.query.all()
    # return render_template("users_index.html", my_users = users)
    return jsonify(users_schema.dump(users))


@users.route("/<int:id>", methods=["GET"])
def user_show(id):
    # user_id = get_jwt_identity()
    # user = User.query.get(user_id)

    # if not user:
    #     return abort(401, description="Invalid user")

    users = Users.query.get(id)
    return render_template("user_show.html", my_user = users)
    # return jsonify(user_schema.dump(users))

@users.route("/<int:id>/watchlists", methods=["GET"])
def user_watchlists_show(id):
    # user_id = get_jwt_identity()
    # # user = User.query.get(user_id)

    # # if not user:
    # #     return abort(401, description="Invalid user")

    user_watchlists = Watchlist.query.filter_by(user_id=id)
    # return jsonify(watchlists_schema.dump(user_watchlists))
    return render_template("user_watchlist.html", my_user_watchlists = user_watchlists)

@users.route("/<int:id>", methods=["PUT", "PATCH"])
def user_update(id):
    pass

@users.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return render_template('home.html')





# @users.route("/auth/logout", methods=["GET"])
# def user_logout():
#     pass

# @users.route("/user/<int:id>", methods=["GET"])
# def user_profile():
#     pass

# @users.route("/user/<int:id>", methods=["PUT", "PATCH"])
# def user_update(id):
#     pass

# @users.route("/user/<int:id>/watchlists/<int:id>", methods=["POST"])
# def user_add_watchlists(id):
#     pass

# @users.route("/user/<int:id>/watchlists/<int:id>/languages/<int:id>", methods=["POST"])
# def user_add_language(id):
#     pass

# @users.route("/user/<int:id>/watchlists/<int:id>", methods=["DELETE"])
# def user_del_watchlists(id):
#     pass