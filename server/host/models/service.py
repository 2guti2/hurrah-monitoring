from server.factories.database import db


class Service(db.Model):
    __tablename__ = 'service'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True)
    host_id = db.Column(db.Integer(), db.ForeignKey('host.id'))
    host = db.relationship('Host', back_populates='services')

    def __init__(self, name, host_id):
        self.name = name
        self.host_id = host_id
