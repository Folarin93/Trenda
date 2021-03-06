import os

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "trenda_is_awesome"
    SECRET_KEY = "trenda_is_awesome"

    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DATABASE_URL")
        if not value:
            raise ValueError("DATABASE_URL is not set")

        return value


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    @property
    def JWT_SECRET_KEY(self):
        value = os.environ.get("JWT_SECRET_KEY")
        if not value:
            raise ValueError("JWT Secret Key is not set")

        return value

class TestingConfig(Config):
    TESTING = True
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        value = os.environ.get("DB_URI_TEST")
        if not value:
            raise ValueError("DB_URI_TEST is not set")

        return value

environment = os.environ.get("FLASK_ENV")

if environment == "production":
    app_config = ProductionConfig()
elif environment == "testing":
    app_config = TestingConfig()
else:
    app_config = DevelopmentConfig()