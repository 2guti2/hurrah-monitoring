from server.factories.database import db
from .service import Service
from ...status.models.report import Report


class Host(db.Model):
    __tablename__ = 'host'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(), unique=True)
    ram = db.Column(db.Float())
    services = db.relationship('Service', back_populates='host')
    reports = db.relationship('Report', back_populates='host')

    def __init__(self, name, ram, services):
        self.name = name
        self.ram = ram
        self.reports = []
        self.services = list(map(lambda dto: Service(dto['name']), services))

    def create_report(self, dto):
        report = Report(dto['timestamp'], dto['usedRamGb'], dto['cpu'], dto['services'])
        self.reports.append(report)
        return report

    def update_services(self, services):
        existing_services_names = list(map(lambda s: s.name, self.services))
        not_present_services = list(filter(lambda s: s['name'] not in existing_services_names, services))
        [self.services.append(Service(new_service['name'])) for new_service in not_present_services]

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'services': list(map(lambda s: s.serialize(), self.services)),
            'reports': len(self.reports)
        }
