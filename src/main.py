from dotenv import load_dotenv
load_dotenv()

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

from flask import Flask
app = Flask(__name__)
app.config.from_object("default_settings.app_config")

from database import init_db
db = init_db(app)

from flask_marshmallow import Marshmallow
mar = Marshmallow(app)

from commands import db_commands
app.register_blueprint(db_commands)

from controllers import registerable_controllers

for controller in registerable_controllers:
    app.register_blueprint(controller)
