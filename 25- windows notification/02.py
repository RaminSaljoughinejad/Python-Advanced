from winotify import Notification
import time
#raw strings = no scaping characters

my_notif = Notification(app_id='my_app',
                        title='My Title',
                        duration="short",
                        msg='My Message',
                        icon=r"C:\Users\Home\Desktop\Python Advanced\windows notification\icon.jpg")

my_notif.show() 