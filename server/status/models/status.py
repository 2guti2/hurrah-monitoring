from server.factories.database import db


class Status(db.Model):
    __tablename__ = 'status'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    is_running = db.Column(db.Boolean())
    report_id = db.Column(db.Integer(), db.ForeignKey('report.id'))
    report = db.relationship('Report', back_populates='statuses')

    def __init__(self, name, is_running):
        self.name = name
        self.is_running = is_running

    def __repr__(self):
        return '<service_status {}>'.format(self.name)

    def serialize(self):
        return {
            'name': self.name,
            'is_running': self.is_running,
        }

    def json_serialize(self):
        return self.serialize()
