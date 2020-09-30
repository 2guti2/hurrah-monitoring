from injector import (Module, singleton)

from .controllers.status_controller import configure_endpoints
from ..factories.database import db
from .services.status_service import StatusService
from ..host.models.host import Host
from ..events.bus import Bus
from ..events.listeners.NewReportListener import NewReportListener


class StatusModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        event_bus = Bus()
        new_report_listener = NewReportListener(self.app)
        event_bus.bind(new_report=new_report_listener.on_new_report)

        service_instance = StatusService(db, Host, event_bus)

        binder.bind(StatusService, to=service_instance, scope=singleton)
        binder.bind(NewReportListener, to=new_report_listener, scope=singleton)
        binder.bind(Bus, to=event_bus, scope=singleton)
        configure_endpoints(self.app)
