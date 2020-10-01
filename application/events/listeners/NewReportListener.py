class NewReportListener:

    def __init__(self, app):
        self.app = app

    # send update to clients via sockets
    def on_new_report(self, **kwargs):
        data = kwargs.get('data')
        print('new report: {}'.format(data.serialize()))
