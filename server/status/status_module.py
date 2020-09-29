from injector import (Module, singleton)

from .models.service_status import ServiceStatus
from .models.status_report import StatusReport
from .controllers.status_controller import configure_endpoints
from ..factories.database import db
from .services.status_service import StatusService


class StatusModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        service_instance = StatusService(db, StatusReport, ServiceStatus)
        binder.bind(StatusService, to=service_instance, scope=singleton)
        configure_endpoints(self.app)
