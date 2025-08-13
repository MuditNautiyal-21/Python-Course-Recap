import time
from plyer import notification

while True:
    print("Its time you drink some water!")
    notification.notify(title="Reminder!",message="Its time you drink some water!")
    time.sleep(60*60)