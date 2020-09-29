from injector import (Module, singleton)

from ..factories.database import db
from .controllers.session_controller import configure_endpoints
from .models.session import Session
from .services.session_service import SessionService


class SessionModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        service_instance = SessionService(db, Session)
        binder.bind(SessionService, to=service_instance, scope=singleton)
        configure_endpoints(self.app)
