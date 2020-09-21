import schedule
import time

def prepJob(job):
    schedule.every(1).minute.do(job)

def initJob():
    schedule.run_pending()
    time.sleep(20)