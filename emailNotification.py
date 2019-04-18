import Facade_API
import urllib.request as ur
import json
from datetime import datetime, timedelta
import pyrebase
from Email import email

class EmailNotifications():
    def __init__(self):
        self.email = email.EmailSend()
        self.API = Facade_API.FacadeAPI()

    def get_dengue_json(self):

        config = {
          "apiKey": "",
          "authDomain": "",
          "databaseURL": "https://data-storage-1205f.firebaseio.com/",
          "storageBucket": ""
        }
        firebase = pyrebase.initialize_app(config)
        db = firebase.database()
        data = db.child("Dengue_Data").get()
        j_data = dict(data.val())

        return j_data


    def timeDefined(self,date):
        y=str(date.year)
        m=str(date.month)
        d=str(date.day)
        if len(d)==1:
            d ='0'+d
        if len(m)==1:
            m ='0'+m
        return str(y)+'-'+str(m)+'-'+str(d)

    def weekDate(self,date):
        date_today = self.timeDefined(date)
        date_prev = self.timeDefined(date - timedelta(days=7))
        return date_prev, date_today

    def isSafePSI(self,value):
        if value<=50:
            return "healthy"
        elif 51<value<=100:
            return "moderate"
        elif 101<value<=200:
            return "unhealthy"
        elif 201<value<=300:
            return "very unhealthy"
        else:
            return "hazardous"

    def isSafePM25(self,value):
        if 0<value<=12:
            return "healthy"
        elif 12<value<=35.4:
            return "moderate"
        elif 35.4<value<=55.4:
            return "unhealthy for sensitive groups"
        elif 55.4<value<=150.4:
            return "unhealthy"
        elif 150.4<value<=250.4:
            return "very unhealthy"
        else:
            return "hazardous"


    def rangeHaze(self):
        date = datetime.now().date()
        date_str= self.weekDate(date)
        today_psi = self.API.getHaze()['psi']['national']
        today_pm25 = self.API.getHaze()['pm25']['national']
        prev_psi = self.API.haze.getJSONHazeRange(date_str[0])['psi']['national']
        prev_pm25 = self.API.haze.getJSONHazeRange(date_str[0])['pm25']['national']
        if today_psi<prev_psi:
            range_str_psi= str(today_psi)+'-'+str(prev_psi)
            maxm_psi = prev_psi
        else:
            range_str_psi= str(prev_psi)+'-'+str(today_psi)
            maxm_psi = today_psi
        if today_pm25<prev_pm25:
            range_str_pm25= str(today_pm25)+'-'+ str(prev_pm25)
            maxm_pm25 = prev_pm25
        else:
            range_str_pm25= str(prev_pm25)+'-'+str(today_pm25)
            maxm_pm25 = today_pm25
        psi_status = self.isSafePSI(maxm_psi)
        pm25_status = self.isSafePM25(maxm_pm25)
        return {'psi':range_str_psi, 'pm25':range_str_pm25, 'psi_status': psi_status, 'pm25_status': pm25_status}

    def getDengue(self):
        j_data = self.get_dengue_json()
        top = j_data['top5_data']
        # print(top)
        table = ''
        for place in top:
            table+="{:s} - {:d} Cases\n".format(place[0],place[1])

        total = j_data['total_cases']
        return (table,total)

    def createMessage(self,date, time, haze, dengue):
        return  "To: PMO\n\nHonorable Prime Minister,\n\nWe respectfully request your attention to the Crisis Management System (CMS) status report on %s at %s which mainly focuses on the emergency situations for the dengue outbreak and haze.\n\nBased on the reported cases, there have been, in total, %s number of dengue outbreaks within Singapore, as of today with the top affected areas:\n\n%s\nMoreover, the psi range for haze has been: %s (%s) and pm25 range %s (%s), this week between %s to %s.\n\nWe are still monitoring the situation and will be sending an updated status report in 30 min time.\n\nRespectfully,\nCrisis Management System Team"%(date, time, dengue[1],dengue[0], haze['psi'], haze['psi_status'], haze['pm25'], haze['pm25_status'], self.weekDate(date)[0], self.weekDate(date)[1])

    def sendEmail(self, recipient, msg, subject):
        server = self.email.startServer()
        status =  self.email.send_email(server,recipient,msg,subject)
        self.email.quitServer(server)
        return status

    def sendNotificationEmail(self,recipient):

        date = datetime.now().date()
        time = str(datetime.now().hour) + ':'+ str(datetime.now().minute)
        haze = self.rangeHaze()
        dengue = self.getDengue()

        subject = "Updated status report on "+ str(date) +" at " + str(time)
        # recipient = ['aditisaini99@gmail.com']
        msg = self.createMessage(date, time, haze, dengue)
        # print(msg)

        self.sendEmail(recipient, msg, subject)

if __name__=='__main__':
    emailnot = EmailNotifications()
    print(emailnot.sendNotificationEmail(['naseerfathima2426@gmail.com']))
    # print(getTop5Dengue())
