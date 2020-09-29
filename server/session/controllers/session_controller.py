import flask
from flask.blueprints import Blueprint
import json
from flask import request
from munch import Munch

from ..services.session_service import SessionService


def configure_endpoints(app):
    sessions_bp = Blueprint('/api/sessions', __name__)

    @sessions_bp.route('/api/sessions', methods=['POST'])
    def get_all(service: SessionService):
        payload = Munch(request.json)
        session = service.create(payload)
        resp = flask.Response(json.dumps(session.serialize()))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    app.register_blueprint(sessions_bp)
