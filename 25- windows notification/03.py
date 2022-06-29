from asyncore import loop
from winotify import Notification, audio
import time
#raw strings = no scaping characters

my_notif = Notification(app_id='my_app',
                        title='My Title',
                        duration="short",
                        msg='My Message',
                        icon=r"C:\Users\Home\Desktop\Python Advanced\windows notification\icon.jpg")

#my_notif.set_audio(audio.Default, loop=False)
#my_notif.set_audio(audio.Default, loop=True)
#my_notif.set_audio(audio.Mail, loop=False)
#my_notif.set_audio(audio.SMS, loop=False)
#my_notif.set_audio(audio.LoopingAlarm, loop=True)#long
my_notif.set_audio(audio.LoopingCall, loop=True)#long

my_notif.show() 