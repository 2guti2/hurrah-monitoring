from server.factories.database import db


class ServiceStatus(db.Model):
    __tablename__ = 'service_status'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    is_running = db.Column(db.Boolean())
    status_report_id = db.Column(db.Integer(), db.ForeignKey('status_report.id'))
    status_report = db.relationship('StatusReport', back_populates='services_status')

    def __init__(self, name, is_running):
        self.name = name
        self.is_running = is_running

    def __repr__(self):
        return '<service_status {}>'.format(self.name)

    def serialize(self):
        return {
            'id': self.id,
            'is_running': self.is_running,
        }

    def json_serialize(self):
        return self.serialize()
