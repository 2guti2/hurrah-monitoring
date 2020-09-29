from .status_controller import configure_status_endpoints
from injector import Module


class StatusModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        configure_status_endpoints(self.app)
