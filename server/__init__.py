from flask import (Flask, render_template)
import os
from flask_cors import CORS
from injector import Injector
from flask_injector import FlaskInjector
from .modules import get_modules


def setup_config(app):
    app.config.from_object(os.environ.get('APP_SETTINGS', 'config.DevelopmentConfig'))


def setup_static_routes(app):
    @app.route('/')
    def my_index():
        return render_template('index.html', flask_token='Hello world')


def setup_app(app):
    CORS(app)
    injector = Injector(get_modules(app))
    FlaskInjector(app=app, injector=injector)


def create_app():
    app = Flask(__name__)
    setup_config(app)
    setup_static_routes(app)
    setup_app(app)
    return app
