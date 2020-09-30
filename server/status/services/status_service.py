class StatusService:
    def __init__(self, db, Report, Host):
        self.db = db
        self.Report = Report
        self.Host = Host

    def create(self, dto):
        report = self.Report(dto['timestamp'], dto['usedRamGb'], dto['cpu'], dto['services'])
        self.db.session.add(report)
        self.db.session.commit()
        return report
