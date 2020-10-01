from threading import Thread
import schedule
import time
from ..status.models.report import Report
from ..status.models.status import Status


def delete_old_reports(app, db):
    with app.app_context():
        Status.query.delete()
        Report.query.delete()
        db.session.commit()


def run_schedule():
    while 1:
        schedule.run_pending()
        time.sleep(1)


class Scheduler:
    def __init__(self, app, db):
        self.app = app
        self.db = db

    def start(self):
        schedule.every().day.at('00:00').do(delete_old_reports, self.app, self.db)
        t = Thread(target=run_schedule)
        t.start()
