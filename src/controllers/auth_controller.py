from main import db
from models.User import Users
from schemas.UserSchema import user_schema, users_schema
from flask import Blueprint, request, jsonify, abort, render_template, redirect, url_for
from main import bcrypt
from flask_login import login_user, current_user, logout_user
from datetime import timedelta
# from flask_jwt_extended import create_access_token

auth = Blueprint('auth', __name__)

@auth.route("/auth/register", methods=["POST"])
def auth_register():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user_username = Users.query.filter_by(username=username).first()
    user_email = Users.query.filter_by(email=email).first()

    if user_username or user_email:
        return abort(400, description="Email or Username already registered")

    user = Users()
    user.username = username
    user.email = email
    user.password = bcrypt.generate_password_hash(password).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    # return jsonify(user_schema.dump(user))
    return redirect(url_for('users.user_show', id=user.id))

    # for testing with insonmia
    # user_fields = user_schema.load(request.json)
    # user_username = Users.query.filter_by(username=user_fields["username"]).first()
    # user_email = Users.query.filter_by(email=user_fields["email"]).first()

    # if user_username or user_email:
    #     return abort(400, description="Email or Username already registered")

    # user = Users()
    # user.username = user_fields["username"]
    # user.email = user_fields["email"]
    # user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")


@auth.route("/auth/login", methods=["POST"])
def auth_login():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    user_username = Users.query.filter_by(username=username).first()
    user_email = Users.query.filter_by(email=email).first()

    if not (user_username and bcrypt.check_password_hash(user_username.password, password)):
        return abort(401, description="Incorrect username or password")

    if not (user_email and bcrypt.check_password_hash(user_email.password, password)):
        return abort(401, description="Incorrect email or password")

    
    login_user(user_username)
    return redirect(url_for('users.user_show', id=user_username.id))

@auth.route("/signup", methods=["GET"])
def signup():
    return render_template('signup.html')

@auth.route("/login", methods=["GET"])
def login():
    return render_template('login.html')






    # user_fields = user_schema.load(request.json)

    # user_username = Users.query.filter_by(username=user_fields["username"]).first()
    # user_email = Users.query.filter_by(email=user_fields["email"]).first()

    # if not (user_username and bcrypt.check_password_hash(user_username.password, user_fields["password"])):
    #     return abort(401, description="Incorrect username or password")

    # if not (user_email and bcrypt.check_password_hash(user_email.password, user_fields["password"])):
    #     return abort(401, description="Incorrect email or password")

    # expiry = timedelta(days = 1)
    # access_token = create_access_token(identity=str(user_email.id), expires_delta=expiry)
    # return jsonify({"token": access_token})