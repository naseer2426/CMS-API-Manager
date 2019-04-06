#Testing shitt
from apscheduler.schedulers.blocking import BlockingScheduler
import SocialMedia_API
import sys



sched = BlockingScheduler()
socialMedia = SocialMedia_API.SocialMedia()



# @sched.scheduled_job('interval', minutes = 1)
# def send_social_media_messages():
#     socialMedia.sendSocialMedia()
#     print("Message sent")
#     sys.stdout.flush()

# @sched.scheduled_job('interval', seconds = 20)
# def send_social_media_messages():
#     print("Clock running!")
#     sys.stdout.flush()
#
# @sched.scheduled_job('interval', minutes = 2)
# def send_social_media_messages():
#     socialMedia.update_dengue_data()
#     print("Dengue data updated")
#     sys.stdout.flush()

sched.start()
