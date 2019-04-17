#Testing shitt
from apscheduler.schedulers.blocking import BlockingScheduler
import SocialMedia_API
import sys



sched = BlockingScheduler()
socialMedia = SocialMedia_API.SocialMedia()



# @sched.scheduled_job('interval', minutes = 5)
# def send_social_media_messages():
#     socialMedia.sendSocialMedia()
#     # socialMedia.send_email(['naseerfathima2426@gmail.com'])
#     print("Social media done!")
#     sys.stdout.flush()

# @sched.scheduled_job('interval', seconds = 20)
# def send_social_media_messages():
#     print("Clock running!")
#     sys.stdout.flush()

@sched.scheduled_job('interval', hours = 24)
def send_social_media_messages():
    socialMedia.update_dengue_data()
    socialMedia.update_haze_data()
    socialMedia.update_cd_data()
    print("Data Updated!")
    sys.stdout.flush()

sched.start()
