from .app_module import AppModule
from .session.session_module import SessionModule
from .status.status_module import StatusModule


def get_modules(app):
    return [StatusModule(app), SessionModule(app), AppModule(app)]
