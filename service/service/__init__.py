from flask import Flask

from .blueprints import api


__version__ = '0.1.0'

def create_app():
    app = Flask(__name__)

    api.init_app(app)

    return app
