"""The app module, containing the app factory function."""
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask

from app import config
from app.api import blueprint as api


def create_app(conf=config.Config):
    """Return an initialized Flask application."""
    app = Flask(__name__)
    app.config.from_object(conf)

    register_blueprints(app)

    handler = RotatingFileHandler('shape_detector.log', maxBytes=10000, backupCount=1)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    return app


def register_blueprints(app):
    """Register blueprints with the Flask application."""
    app.register_blueprint(api, url_prefix='/shape')
    return None
