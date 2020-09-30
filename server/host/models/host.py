from server.factories.database import db
# important ref
from .service import Service


class Host(db.Model):
    __tablename__ = 'host'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True)
    ram = db.Column(db.Float())
    services = db.relationship('Service', back_populates='host')

    def __init__(self, name, ram):
        self.name = name
        self.ram = ram
