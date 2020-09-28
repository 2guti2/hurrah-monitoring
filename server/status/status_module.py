from .status_controller import configure_status_endpoints


def configure_status_module(app):
    configure_status_endpoints(app)
