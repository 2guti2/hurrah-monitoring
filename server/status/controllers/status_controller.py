import flask
from flask.blueprints import Blueprint
import json
from flask import request

from server.status.services.status_service import StatusService


def configure_endpoints(app):
    status_bp = Blueprint('/api/statuses', __name__)

    @status_bp.route('/api/statuses', methods=['GET'])
    def get_status(service: StatusService):
        host_id = request.args.get('hostId', None)
        reports = service.get_all(host_id)
        serialized = list(map(lambda report: report.serialize(), reports))
        resp = flask.Response(json.dumps(serialized))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    @status_bp.route('/api/statuses', methods=['POST'])
    def new_status(service: StatusService):
        status = service.create(request.json)
        resp = flask.Response(json.dumps(status.serialize()))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    app.register_blueprint(status_bp)
