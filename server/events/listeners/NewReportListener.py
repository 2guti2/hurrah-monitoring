class NewReportListener:

    def __init__(self, app):
        self.app = app

    def on_new_report(self, *args, **kwargs):
        data = kwargs.get('data')
        print('new report: {}'.format(data))
