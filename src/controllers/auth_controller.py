from main import db
from models.User import Users
from schemas.UserSchema import user_schema, users_schema
from flask import Blueprint, request, jsonify, abort, render_template
from main import bcrypt

auth = Blueprint('auth', __name__,url_prefix="/auth")

@auth.route("/signup", methods=["POST"])
def auth_register():
    user_fields = user_schema.load(request.json)

    user_username_checkuser = Users.query.filter_by(username=user_fields["username"]).first()
    user_email_check = Users.query.filter_by(email=user_fields["email"]).first()

    if user_username_checkuser or user_email_check:
        return abort(400, description="Email or Username already registered")

    user = Users()
    user.username = user_fields["username"]
    user.email = user_fields["email"]
    user.password = bcrypt.generate_password_hash(user_fields["password"]).decode("utf-8")

    db.session.add(user)
    db.session.commit()

    return jsonify(user_schema.dump(user))

@auth.route("/login", methods=["POST"])
def auth_login():
    user_fields = user_schema.load(request.json)

    user_username_checkuser = Users.query.filter_by(username=user_fields["username"]).first()
    user_email_check = Users.query.filter_by(email=user_fields["email"]).first()

    if not (user_username_checkuser and bcrypt.check_password_hash(user_username_checkuser.password, user_fields["password"])):
        return abort(401, description="Incorrect username or password")

    if not (user_email_check and bcrypt.check_password_hash(user_email_check.password, user_fields["password"])):
        return abort(401, description="Incorrect email or password")

    return "token"

