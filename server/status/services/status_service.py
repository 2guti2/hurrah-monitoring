
class StatusService:
    def __init__(self, db, StatusReport, Host):
        self.db = db
        self.StatusReport = StatusReport
        self.Host = Host

    def create(self, dto):
        report = self.StatusReport(dto['timestamp'], dto['usedRamGb'], dto['cpu'], dto['services'])
        self.db.session.add(report)
        self.db.session.commit()
        return report
