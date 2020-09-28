import flask
from flask.blueprints import Blueprint
import json


def configure_status_endpoints(app):
    status_bp = Blueprint('/status', __name__)

    @status_bp.route('/status', methods=['GET'])
    def get_status():
        response = ['status1', 'status2']
        resp = flask.Response(json.dumps(response))
        resp.headers['Content-Type'] = 'application/json'
        return resp

    app.register_blueprint(status_bp)
