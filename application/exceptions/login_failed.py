import werkzeug


class LoginFailed(werkzeug.exceptions.HTTPException):
    code = 404
    description = 'login failed'