
class StatusService:
    def __init__(self, db, StatusReport, ServiceStatus):
        self.db = db
        self.StatusReport = StatusReport
        self.ServiceStatus = ServiceStatus

    def create(self, dto):
        report = self.map(dto)
        self.db.session.add(report)
        self.db.session.commit()
        return report

    def map(self, dto):
        report = self.StatusReport(dto['timestamp'], dto['usedRamGb'], dto['cpu'])
        statuses = []
        for s in dto['services']:
            statuses.append(self.ServiceStatus(s['name'], s['running']))
        report.services_status = statuses
        return report
