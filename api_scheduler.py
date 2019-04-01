#Testing shitt
from apscheduler.schedulers.blocking import BlockingScheduler
import SocialMedia_API
import sys



sched = BlockingScheduler()
socialMedia = SocialMedia_API.SocialMedia()



@sched.scheduled_job('interval', hours=24)
def send_social_media_messages():
    socialMedia.sendSocialMedia()
    print("Message sent")
    sys.stdout.flush()

@sched.scheduled_job('cron', hour=13)
def send_social_media_messages():
    socialMedia.update_dengue_data()
    print("Message sent")
    sys.stdout.flush()

sched.start()
