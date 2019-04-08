#The socialMedia only outputs the changes in PSI for now.
import Facade_API
import emailNotification as email
import datetime

class SocialMedia(object):
    def __init__(self):
        self.API = Facade_API.FacadeAPI()
    def create_message(self,messages):
        self.now = datetime.datetime.now()
        self.date = datetime.datetime.now().date()
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
            time = self.getTime()
            dt=self.timeDefined(self.date)
            dengue_data = self.getDengueInfo()
            total_dengue_cases = dengue_data[1]
            dengue_table = dengue_data[0]
            msg = 'Update as of ' +dt+ ' at '+ time +".\n\nDENGUE INFORMATION\n\nThere have been a total of "+str(total_dengue_cases)+" reports of dengue outbreaks all around Singapore. The top 5 places in Singapore with most cases of Dengue outbreaks are as follows:\n"+dengue_table+"\nHAZE INFORMATION\n\n24-hour Haze PSI reading " + air_status + ".\n24-hr PSI Area: " + psi_message + ".\n1-hr PM2.5 PSI Area: " + pm25_message
            return msg
        else:
            #Add stuff here
            return messages

    def timeDefined(self,date):
        y=str(self.date.year)
        m=str(self.date.month)
        d=str(self.date.day)
        if len(d)==1:
            d ='0'+d
        if len(m)==1:
            m ='0'+m
        return str(d)+'-'+str(m)+'-'+str(y)

    def getTime(self):
        h=str(self.now.hour)
        m=str(self.now.minute)
        s=str(self.now.second)
        if len(h)==1:
            h='0'+h;
        if len(m)==1:
            h='0'+m;
        if len(s)==1:
            h='0'+s;
        return str(h)+':'+str(m)+':'+str(s)

    def getDengueInfo(self):
        j_data = self.API.dengue.j_data
        top = j_data['top5_data']
        # print(top)
        table = ''
        for place in top:
            table+="{:s} - {:d} Cases\n".format(place[0],place[1])

        total = j_data['total_cases']
        return (table,total)

    def sendSocialMedia(self,sender = '+12052939421',receiver_list = ['+6583676240','+6596579895','+6586502577'],extra_messages=None):
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
        email.sendNotificationEmail(recipient)

if __name__ == "__main__":
    socialMedia = SocialMedia()
    socialMedia.sendSocialMedia()
"""
OUTPUT:
The air quality is healthy.
The psi is:  national - 61 east - 57 south - 58 central - 61 west - 55 north - 52.
The pm25 is:  national - 21 east - 18 south - 18 central - 21 west - 15 north - 13
"""
