from main import mar
from models.User import Users
from models.Watchlist import Watchlist

class UserSchema(mar.SQLAlchemyAutoSchema):
    class Meta:
        model = Users

user_schema = UserSchema()
users_schema = UserSchema(many=True)