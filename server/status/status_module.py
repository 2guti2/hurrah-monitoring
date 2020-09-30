from injector import (Module, singleton)

from .models.report import Report
from .controllers.status_controller import configure_endpoints
from ..factories.database import db
from .services.status_service import StatusService
from ..host.models.host import Host


class StatusModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        service_instance = StatusService(db, Report, Host)
        binder.bind(StatusService, to=service_instance, scope=singleton)
        configure_endpoints(self.app)
