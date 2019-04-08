from twilio.rest import Client

class SMSAPI:
    def __init__(self):
        self.account_sid ='ACa81b7b9e04c7af554434a5709cbcb7d4'
        self.auth_token = '9843de1aba89dd24ca1eaada537154e8'
    def sendSMS(self, textMessage, sender, receiver):
        # try:
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
                    body=textMessage,
                    from_=sender,
                    to=receiver
                    )
        return "SMS sent"
        # except:
        #     return "SMS failed to send"

if __name__ == '__main__':
    s = SMSAPI()
    print(s.sendSMS('test','+12052939421',['+6583676240','+6596579895','+6586502577']))
