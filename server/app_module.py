from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton
from server.factories.database import db, migrate


class AppModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        db_instance = self.configure_db(self.app)
        binder.bind(SQLAlchemy, to=db_instance, scope=singleton)

    def configure_db(self, app):
        db.init_app(app)
        migrate.init_app(app, db)
        return db
