import flask
from flask.blueprints import Blueprint
import json

from ..services.host_service import HostService


def configure_endpoints(app):
    hosts_bp = Blueprint('/api/hosts', __name__)

    @hosts_bp.route('/api/hosts', methods=['GET'])
    def get_all(service: HostService):
        hosts = service.get_all()
        serialized = list(map(lambda host: host.serialize(), hosts))
        resp = flask.Response(json.dumps(serialized))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    app.register_blueprint(hosts_bp)
