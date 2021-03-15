from main import mar
from models.User import Users
from models.Watchlist import Watchlist
from marshmallow.validate import Email, Length

class UserSchema(mar.SQLAlchemyAutoSchema):
    class Meta:
        model = Users
        load_only = ["password"]

    email = mar.String(required=True, validate=[Length(min=5), Email()])
    username = mar.String(required=True, validate=Length(min=5))
    password = mar.String(required=True, validate=Length(min=6))

user_schema = UserSchema()
users_schema = UserSchema(many=True)