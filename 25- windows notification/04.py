from asyncore import loop
from winotify import Notification, audio
import time
#raw strings = no scaping characters

my_notif = Notification(app_id='my_app',
                        title='My Title',
                        duration="short",
                        msg='My Message',
                        icon=r"C:\Users\Home\Desktop\Python Advanced\windows notification\icon.jpg")

my_notif.set_audio(audio.Default, loop=False)
my_notif.add_actions(label="Click Me!", launch="https://www.google.com")

my_notif.show() 