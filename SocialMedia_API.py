#The socialMedia only outputs the changes in PSI for now.
import Facade_API
from EmailNotifications import email

class SocialMedia(object):
    def __init__(self):
        self.API = Facade_API.FacadeAPI()
    def create_message(self,messages):
        now = datetime.datetime.now()
        date = datetime.now().date()
        if messages == None:
            haze_details = self.API.getHaze()
            air_status = haze_details['air_status']
            pm25 = haze_details['pm25']
            psi = haze_details['psi']
            psi_message = ""
            pm25_message = ""
            for k,v in psi.items():
                psi_message = psi_message + " "+ k + " - " + str(v)
            for k,v in pm25.items():
                pm25_message = pm25_message + " "+ k + " - " + str(v)
            time = getTime()
            dt=timeDefined(date)
            msg = 'Update as of ' +dt+ ' at '+ time +"\n24-hour Haze PSI reading " + air_status + ".\n24-hr PSI Area: " + psi_message + ".\n1-hr PM2.5 PSI Area: " + pm25_message

        else:
            #Add stuff here
            return messages

    def timeDefined(date):
        y=str(date.year)
        m=str(date.month)
        d=str(date.day)
        if len(d)==1:
            d ='0'+d
        if len(m)==1:
            m ='0'+m
        return str(y)+'-'+str(m)+'-'+str(d)

    def getTime():
        h=str(now.hour)
        m=str(now.minute)
        s=str(now.second)
        if len(h)==1:
            h='0'+h;
        if len(m)==1:
            h='0'+m;
        if len(s)==1:
            h='0'+s;
        return str(h)+':'+str(m)+':'+str(s)

    def sendSocialMedia(self,sender = '+12565769037',receiver_list = ['+6583676240','+6596579895'],extra_messages=None):
        #We can add additional details using extra_messages
        #Craft a message to send to all social medias

        message = self.create_message(extra_messages)
        #Sending to all social Medias
        for receiver in receiver_list:
           self.API.sendSMS(message, sender, receiver)
        self.API.sendTwitter(message)
        self.API.sendTelegram(message)

    def get_dengue_data(self):
        return self.API.getDengue()

    def update_dengue_data(self):
        return self.API.updateDengue()

    def send_email(self,recipient):
        email.sendNotificationEmail()

if __name__ == "__main__":
    socialMedia = SocialMedia()
    socialMedia.update_dengue_data()
"""
OUTPUT:
The air quality is healthy.
The psi is:  national - 61 east - 57 south - 58 central - 61 west - 55 north - 52.
The pm25 is:  national - 21 east - 18 south - 18 central - 21 west - 15 north - 13
"""
