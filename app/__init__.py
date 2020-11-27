# app/__init__.py

# third-party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

# local imports
from config import app_config


# db variable initialization
db = SQLAlchemy()
ma = Marshmallow()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    migrate = Migrate(app, db)

    from . import models

    from .user import user as user_blueprint
    app.register_blueprint(user_blueprint)

    from .product import product as product_blueprint
    app.register_blueprint(product_blueprint)

    from .order import order as order_blueprint
    app.register_blueprint(order_blueprint)

    from .cart import cart as cart_blueprint
    app.register_blueprint(cart_blueprint)

    return app