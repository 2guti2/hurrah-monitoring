from werkzeug.wrappers import Request, Response
import json

from .session.models.session import Session
from .session.services.session_service import SessionService


class AuthMiddleware:
    def __init__(self, wsgi_app, app, db):
        self.wsgi_app = wsgi_app
        self.app = app
        self.session_service = SessionService(db, Session)

    def __call__(self, environ, start_response):
        request = Request(environ)
        token = request.headers.get('Authorization', None)

        if self.is_authorized(token, request.path):
            return self.wsgi_app(environ, start_response)

        res = Response(json.dumps({'message': 'Authorization failed'}), mimetype='text/plain', status=401)
        return res(environ, start_response)

    def is_authorized(self, token, path):
        return path == '/api/sessions' or path == '/' or (
            token is not None and
            self.session_service.is_authorized(self.app, token)
        )
