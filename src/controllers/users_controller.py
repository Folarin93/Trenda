from main import db
from models.User import Users
from schemas.UserSchema import user_schema, users_schema
from flask import Blueprint, request, jsonify

users = Blueprint('users', __name__, url_prefix="/users")

@users.route("/", methods=["GET"])
def user_index():
    users = Users.query.all()
    return jsonify(users_schema.dump(users))


@users.route("/<int:id>", methods=["GET"])
def user_show(id):
    users = Users.query.get(id)
    return jsonify(user_schema.dump(users))