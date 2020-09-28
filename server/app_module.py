from injector import Module
from .status.status_module import configure_status_module


class AppModule(Module):
    def __init__(self, app):
        self.app = app

    def configure(self, binder):
        configure_status_module(self.app)
