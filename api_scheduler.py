#Testing shitt
from apscheduler.schedulers.blocking import BlockingScheduler
import SocialMedia_API
import Facade_API
import sys

sched = BlockingScheduler()
socialMedia = SocialMedia_API.SocialMedia()
facadeAPI = Facade_API.FacadeAPI()

 @sched.scheduled_job('interval', minutes = 30)
 def send_social_media_messages():
     socialMedia.sendSocialMedia()
     socialMedia.send_email(['naseerfathima2426@gmail.com'])
     print("Social media done!")
     sys.stdout.flush()

 @sched.scheduled_job('interval', minutes = 30)
 def send_social_media_messages():
     facadeAPI.updateHaze()
     print("Haze updated!")
     sys.stdout.flush()


@sched.scheduled_job('interval', hours = 24)
def send_social_media_messages():
    facadeAPI.updateDengue()
    facadeAPI.updateCD()
    print("Data Updated!")
    sys.stdout.flush()

sched.start()
