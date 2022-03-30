from twilio.rest import Client
from twilio.twiml.voice_response import Dial, Play, Pause, VoiceResponse, Say
import os, time, random
class CommunicationsOperator():
    def __init__(self): 
        self.account_SID = "YourAuthToken" #os.environ["TWILIO_ACCOUNT_SID"]
        self.from_num = "YourTwilio#" #Has to be a safer way to do this 
        self.to_num = str
        self.auth_tok = "YourTwilioAuthToken"#os.environ["TWILIO_AUTH_TOKEN"]
        self.client = Client(self.account_SID, self.auth_tok)
        self.to_list = []
      
    def voice():
        resp = VoiceResponse()
        resp.say("")

        return str(resp)
    def send_call(self, msg = None, to_num = None):
        print("Creating call...")
        
        twiml_msg = VoiceResponse()
        twiml_msg.pause(length = 5)
        twiml_msg.say(msg)

        self.to_num = to_num
        call = self.client.calls.create(
            to = self.to_num,
            from_ = self.from_num,
            #twi message link??? 
            twiml = twiml_msg
            )
        
        print(call.sid)
        print("Call finished sending.")

    def send_sms(self, msg, to_num = None):
        txt = str(msg)
        self.to_num = to_num
        print("Sending message...")
        message = self.client.messages.create(
            body = txt,
            from_ = self.from_num,
            to = self.to_num
            )
        print(message.sid)
        print(txt)
        print("Message sent.")
#Run template   
#co = CommunicationsOperator()
#co.send_sms()
#co.send_sms("YourMessage", "Number to send to")
#co.send_call("Your message", "Number to send to")

