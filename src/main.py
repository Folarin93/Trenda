from dotenv import load_dotenv
load_dotenv()

from flask import Flask
# from flask import Flask, jsonify
# from marshmallow.exceptions import ValidationError
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
# from flask_migrate import Migrate

db = SQLAlchemy()
mar = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()
login_manager = LoginManager()
login_manager.login_view = "auth.login"
# migrate = Migrate()


def create_app():
    #Flask applcation creation
    app = Flask(__name__)
    app.config.from_object("default_settings.app_config")

    #Database connection
    db.init_app(app)

    #Setup Serializaition & Deserialization
    mar.init_app(app)

    bcrypt.init_app(app)
    jwt.init_app(app)
    login_manager.init_app(app)
    # migrate.init_app(app, db)

    from models.User import get_user
    
    @login_manager.user_loader
    def load_user(user_id):
        return get_user(user_id)

    #Flask commands for database
    from commands import db_commands
    app.register_blueprint(db_commands)

    #Controller registration
    from controllers import registerable_controllers

    for controller in registerable_controllers:
        app.register_blueprint(controller)
    
    return app