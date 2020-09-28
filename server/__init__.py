from flask import (Flask, render_template)
import os
from flask_cors import CORS
from injector import Injector
from flask_injector import FlaskInjector
from .app_module import AppModule


def setup_config(app):
    app.config.from_object(os.environ['APP_SETTINGS'])


def setup_static_routes(app):
    @app.route('/')
    def my_index():
        return render_template('index.html', flask_token='Hello world')


def setup_app(app):
    CORS(app)
    injector = Injector([AppModule(app)])
    FlaskInjector(app=app, injector=injector)


def create_app():
    app = Flask(__name__)
    setup_config(app)
    setup_static_routes(app)
    setup_app(app)
    return app
