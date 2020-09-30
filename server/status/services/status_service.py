class StatusService:
    def __init__(self, db, Report, Host, bus):
        self.db = db
        self.Report = Report
        self.Host = Host
        self.bus = bus

    def create(self, dto):
        host = self.__get_or_create_host(dto)
        host.create_report(dto)
        self.__save_host(host)
        return host

    def __get_or_create_host(self, dto):
        host = self.Host.query.filter_by(name=dto['hostname']).first()
        if host is None:
            host = self.Host(dto['hostname'], dto['totalRamGb'], dto['services'])
        return host

    def __save_host(self, host):
        self.db.session.add(host)
        self.db.session.commit()
