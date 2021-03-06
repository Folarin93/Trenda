from main import db
from models.Language import Languages
from schemas.LanguageSchema import language_schema, languages_schema
from flask import Blueprint, request, jsonify

languages = Blueprint('languages', __name__, url_prefix="/languages")

@languages.route("/", methods=["GET"])
def language_index():
    languages = Languages.query.all()
    return jsonify(languages_schema.dump(languages))


@languages.route("/<int:id>", methods=["GET"])
def language_show(id):
    languages = Languages.query.get(id)
    return jsonify(language_schema.dump(languages))