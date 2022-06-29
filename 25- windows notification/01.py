# pip install winotify


from winotify import Notification
import time


my_notif = Notification(app_id='my_app',
                        title='My Title',
                        duration="short",#short, long
                        msg='My Message')

my_notif.show()



