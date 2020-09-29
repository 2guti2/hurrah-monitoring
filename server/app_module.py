from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

from server.exceptions.login_failed import LoginFailed
from server.factories.database import db, migrate


def handle_login_failed(e):
    return {'message': e.description}, e.code


class AppModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        db.init_app(self.app)
        migrate.init_app(self.app, db)
        binder.bind(SQLAlchemy, to=db, scope=singleton)
        self.app.register_error_handler(LoginFailed, handle_login_failed)
