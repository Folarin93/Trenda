from main import db
from models.User import Users
from schemas.UserSchema import user_schema, users_schema
from models.Watchlist import Watchlist
from schemas.WatchlistSchema import watchlist_schema, watchlists_schema
from models.Language import Languages
from schemas.LanguageSchema import language_schema, languages_schema
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for, flash
from main import bcrypt
from flask_login import login_user, current_user, logout_user, login_required
from datetime import timedelta


auth = Blueprint('auth', __name__)

@auth.route("/auth/register", methods=["POST"])
def auth_register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user_username = Users.query.filter_by(username=username).first()
    user_email = Users.query.filter_by(email=email).first()

    if user_username or user_email:
        flash("Username/email already exists", "info")
        return redirect(url_for('auth.signup'))

    elif (len(username) or len(email)) < 5 or (len(password)) < 6:
        flash("Username/email/password min 6 Characters", "info")
        return redirect(url_for('auth.signup'))



    user = Users()
    user.username = username
    user.email = email
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    languages = Languages.query.all()
    for lang in languages:
        user_watchlist = Watchlist()
        user_watchlist.user_id = user.id
        user_watchlist.language_id = lang.id
        db.session.add(user_watchlist)
    db.session.commit()

    flash("Successfuly registered! Please Log in", "info")
    return redirect(url_for('users.profile', id=user.id))


@auth.route("/auth/login", methods=["POST"])
def auth_login():
    username = request.form.get('username')
    password = request.form.get('password')

    user_username = Users.query.filter_by(username=username).first()

    if not (user_username and bcrypt.check_password_hash(user_username.password, password)):
        flash("Incorrect Login", "info")
        return redirect(url_for('auth.login'))
    
    login_user(user_username)
    return redirect(url_for('users.profile', id=user_username.id))

@auth.route("/signup", methods=["GET"])
def signup():
    return render_template('signup.html')

@auth.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

@auth.route("/home", methods=["GET"])
def home():
    return render_template('home.html')


@auth.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return render_template('home.html')


