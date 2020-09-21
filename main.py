import scheduler
import notification

scheduler.prepJob(notification.notify)

while True:
    scheduler.initJob()