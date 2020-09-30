class StatusService:
    def __init__(self, db, Host, bus):
        self.db = db
        self.Host = Host
        self.bus = bus

    def create(self, dto):
        host = self.__create_or_update_host(dto)
        report = host.create_report(dto)
        self.__save_host(host)
        self.bus.emit('new_report', data=host)
        return report

    def __create_or_update_host(self, dto):
        host = self.Host.query.filter_by(name=dto['hostname']).first()
        if host is None:
            host = self.Host(dto['hostname'], dto['totalRamGb'], dto['services'])
        else:
            host.update_services(dto['services'])
        return host

    def __save_host(self, host):
        self.db.session.add(host)
        self.db.session.commit()
