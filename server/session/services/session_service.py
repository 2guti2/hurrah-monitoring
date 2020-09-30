from server.exceptions.login_failed import LoginFailed


def login_succeeds(user):
    return user['username'] == 'admin' and user['password'] == 'Passw0rd!'


class SessionService:
    def __init__(self, db, Session):
        self.db = db
        self.Session = Session

    def create(self, user):
        if not login_succeeds(user):
            raise LoginFailed()

        session = self.Session.query.first()

        if session is None:
            session = self.Session()
            self.db.session.add(session)
            self.db.session.commit()

        return session

    def is_authorized(self, token):
        return self.Session.query.filter_by(token=token).first() is not None
