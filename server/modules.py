from .app_module import AppModule
from .status.status_module import StatusModule


def get_modules(app):
    return [StatusModule(app), AppModule(app)]
