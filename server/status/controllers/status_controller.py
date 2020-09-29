import flask
from flask.blueprints import Blueprint
import json
from flask import request

from server.status.services.status_service import StatusService


def configure_endpoints(app):
    status_bp = Blueprint('/api/statuses', __name__)

    @status_bp.route('/api/statuses', methods=['GET'])
    def get_status():
        response = ['status1', 'status2']
        resp = flask.Response(json.dumps(response))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    @status_bp.route('/api/statuses', methods=['POST'])
    def new_status(service: StatusService):
        report = service.create(request.json)
        resp = flask.Response(json.dumps(report.serialize()))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    app.register_blueprint(status_bp)
