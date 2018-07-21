from flask import Flask

from pyromatic.rest import storageroom
from pyromatic.settings import DevConfig


def create_app(config_object=DevConfig):
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.register_blueprint(storageroom.blueprint)
    return app
