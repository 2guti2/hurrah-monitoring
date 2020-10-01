import flask
from flask.blueprints import Blueprint
import json
from flask import request

from ..services.session_service import SessionService


def configure_endpoints(app):
    sessions_bp = Blueprint('/api/sessions', __name__)

    @sessions_bp.route('/api/sessions', methods=['POST'])
    def get_all(service: SessionService):
        session = service.create(request.json)
        resp = flask.Response(json.dumps(session.serialize()))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    app.register_blueprint(sessions_bp)
