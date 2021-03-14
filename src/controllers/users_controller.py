from main import db
from models.User import Users
from schemas.UserSchema import user_schema, users_schema
from models.Watchlist import Watchlist
from schemas.WatchlistSchema import watchlist_schema, watchlists_schema
from models.Language import Languages
from schemas.LanguageSchema import language_schema, languages_schema
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from details import details


users = Blueprint('users', __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def user_index():
    users = Users.query.all()
    # return render_template("users_index.html", my_users = users)
    return jsonify(users_schema.dump(users))

@users.route("/<int:id>", methods=["GET"])
@login_required
def profile(id):
    users = Users.query.get(id)
    return render_template("user_profile.html", my_user = users)

@users.route("/<int:id>/details", methods=["GET"])
@login_required
def user_show(id):
    users = Users.query.get(id)
    return render_template("user_show.html", my_user = users)


@users.route("/<int:id>", methods=["POST"])
@login_required
def user_update(id):
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    phone = request.form.get('phone')

    my_user = Users()
    my_user.username = username
    my_user.email = email
    my_user.password = bcrypt.generate_password_hash(password).decode("utf-8")
    my_user.first_name = first_name
    my_user.last_name = last_name
    my_user.phone = phone

    db.session.add(user)
    db.session.commit()

    return render_template('user_show.html', id=my_user.id)

@users.route("/<int:id>/watchlists", methods=["GET"])
@login_required
def user_watchlists_show(id):
    users = Users.query.get(id)
    user_watchlists = Watchlist.query.filter_by(user_id=id)
    language_info = details()

    return render_template("user_watchlist.html", my_user_watchlists = user_watchlists, my_user = users, language_info = language_info)

@users.route("/<int:id>/watchlists/languages", methods=["GET"])
@login_required
def user_languages(id):
    languages = Languages.query.all()
    user_languages = Watchlist.query.filter_by(user_id=id)
    add_languages = []
    
    for lang in languages:
        language = Watchlist.query.filter_by(language_id=lang.id, user_id=id).first()
        if not language: 
            add_languages.append(lang)
        

    return render_template("languages.html", add_languages = add_languages, my_languages = user_languages, id=current_user.id)


# @users.route("/user/<int:id>/watchlists/<int:id>", methods=["POST"])
# def user_add_watchlists(id):
#     pass

# @users.route("/user/<int:id>/watchlists/<int:id>/languages/<int:id>", methods=["POST"])
# def user_add_language(id):
#     pass

# @users.route("/user/<int:id>/watchlists/<int:id>", methods=["DELETE"])
# def user_del_watchlists(id):
#     pass