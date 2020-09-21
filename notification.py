from notifypy import Notify

def notify():
    notification = Notify()
    notification.title = "Water Alert!"
    notification.message = "Go get some water."
    notification.icon = "icon.png"
    notification.send()