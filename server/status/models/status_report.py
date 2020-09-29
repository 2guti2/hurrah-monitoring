from server.factories.database import db


class StatusReport(db.Model):
    __tablename__ = 'status_report'

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime())
    ram = db.Column(db.Float())
    cpu = db.Column(db.Float())
    services_status = db.relationship('ServiceStatus', back_populates='status_report')

    def __init__(self, timestamp, ram, cpu):
        self.timestamp = timestamp
        self.ram = ram
        self.cpu = cpu

    def __repr__(self):
        return '<id {}>'.format(self.id)

    def serialize(self):
        return {
            'id': self.id,
            'is_running': self.is_running,
        }

    def json_serialize(self):
        return self.serialize()
