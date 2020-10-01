from injector import (Module, singleton)

from ..factories.database import db
from .controllers.host_controller import configure_endpoints
from .models.host import Host
from .services.host_service import HostService


class HostModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        service_instance = HostService(db, Host)
        binder.bind(HostService, to=service_instance, scope=singleton)
        configure_endpoints(self.app)
