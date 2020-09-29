from server.factories.database import db


class StatusReport(db.Model):
    __tablename__ = 'status_report'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    timestamp = db.Column(db.DateTime())
    ram = db.Column(db.Float())
    cpu = db.Column(db.Float())
    services_status = db.relationship('ServiceStatus', back_populates='status_report')

    def __init__(self, timestamp, ram, cpu, services):
        self.timestamp = timestamp
        self.ram = ram
        self.cpu = cpu
        statuses = []
        for s in services:
            statuses.append(self.ServiceStatus(s['name'], s['running']))
        self.services_status = statuses

    def __repr__(self):
        return '<status_report {}>'.format(self.timestamp)

    def serialize(self):
        return {
            'id': self.id,
            'timestamp': str(self.timestamp),
            'ram': self.ram,
            'cpu': self.cpu
        }
