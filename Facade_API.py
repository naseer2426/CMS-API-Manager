from Haze import Haze
from Dengue import dengue_api
from CD_Shelter import CD_Shelter_API

class FacadeAPI(object):
    def __init__(self):
        self.haze = Haze.HazeAPI()
        self.dengue = dengue_api.Dengue()
        self.cd_shelter = CD_Shelter_API.CDShelter()
        #self.SMS = SMS.SMSAPI()
        #self.twitter = twitter.TwitterAPI()
        # self.email = email.EmailSend()
        #self.telegram_api = telegram_api.TelegramAPI()

    def getHaze(self):
        return self.haze.getJSON()

    def updateHaze(self):
        return self.haze.write_firebase()

    def getDengue(self):
        self.dengue_data = self.dengue.get_polygon_data()
        return self.dengue_data

    def updateDengue(self):
        return self.dengue.write_firebase()

    def getCDShelterData(self):
        return self.cd_shelter.get_cd_shelter_locations()

    def updateCD(self):
        return self.cd_shelter.write_firebase()

    #def sendSMS(self,textMessage, sender, receiver):
    #    return self.SMS.sendSMS(textMessage, sender, receiver)

    #def sendTwitter(self,message):
    #    return self.twitter.sendTweet(message)

    # def sendEmail(self, recipient, msg, subject):
    #    self.server = email.EmailSend.startServer()
    #    to_return =  self.email.send_email(self.server,recipient,msg,subject)
    #    self.email.quitServer(self.server)
    #    return to_return

    #def sendTelegram(self,message):
    #    return self.telegram_api.sendTelegramMessage(message)

if __name__ == "__main__":
    API = FacadeAPI()
    API.updateCD()
    API.updateHaze()
    API.updateDengue()
    print("Done")

    #Get the JSON for haze
    #print(API.getHaze())

    #Get the JSON for dengue
    #print(API.getDengue())

    #Sending SMS
    #print(API.sendSMS("this is a test message",'+12565769037','+65 9657 9895'))

    #Sending Tweet
    #print(API.sendTwitter("This is a test Message"))

    #Sending Email
    #print(API.sendEmail(['rainscindo@gmail.com'], "Greetings","Subject Title"))

    #Sending message on telegram
    #print(API.sendTelegram('This is a test message'))
