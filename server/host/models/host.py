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

    def __init__(self, name, ram, service_dtos):
        self.name = name
        self.ram = ram
        self.reports = []
        services = []
        for s in service_dtos:
            services.append(Service(s['name']))
        self.services = services

    def create_report(self, dto):
        report = Report(dto['timestamp'], dto['usedRamGb'], dto['cpu'], dto['services'])
        self.reports.append(report)
        return report
