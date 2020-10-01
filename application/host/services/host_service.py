class HostService:
    def __init__(self, db, Host):
        self.db = db
        self.Host = Host

    def get_all(self):
        return self.Host.query.all()
