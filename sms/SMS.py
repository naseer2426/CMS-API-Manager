from twilio.rest import Client

class SMSAPI:
    def __init__(self):
        self.account_sid ='AC78f830984dab0f546591b5125785752f'
        self.auth_token = '8ea129a7c9059dead55d8d72fee69ff6'
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
