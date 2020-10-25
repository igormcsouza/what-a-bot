from flask import Blueprint
from flask_restful import Api

from .v1.resources.subjects import SubjectResource


bp = Blueprint("api-v1", __name__, url_prefix="/api/v1")
api = Api(bp)
api.add_resource(SubjectResource, '/subject')

def init_app(app):
    app.register_blueprint(bp)