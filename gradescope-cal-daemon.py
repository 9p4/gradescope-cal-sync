from gradescopecalendar.gradescopecalendar import GradescopeCalendar
import logging
from dotenv import load_dotenv
import os
from apscheduler.schedulers.blocking import BlockingScheduler

load_dotenv()

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")
PATH = os.getenv("CALPATH")
IS_INSTRUCTOR = os.getenv("IS_INSTRUCTOR") == "True"
LOGGING_ENABLED = True
LOGGING_LEVEL = logging.INFO

sched = BlockingScheduler()


def update():
    calendar = GradescopeCalendar(EMAIL, PASSWORD, IS_INSTRUCTOR)
    calendar.write_to_ical(PATH)


def run():
    os.path.exists(PATH) or os.mkdir(PATH)
    logger = logging.getLogger("gradescopecalendar" if LOGGING_ENABLED else None)
    logger.setLevel(LOGGING_LEVEL)
    update()
    sched.add_job(update, 'interval', hours=1)
    sched.start()


if __name__ == "__main__":
    run()
