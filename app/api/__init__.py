"""API init file."""
from flask import Blueprint
from flask_restplus import Api
from app.api.routes import ns


blueprint = Blueprint('api', __name__)
api = Api(blueprint,
          version='0.1', title='Shape Detector',
          description='Simple shape detection <style>.models {display: none !important}</style> .',
          doc='/doc')
api.add_namespace(ns)
