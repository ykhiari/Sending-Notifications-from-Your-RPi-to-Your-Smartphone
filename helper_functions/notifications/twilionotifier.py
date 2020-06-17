from twilio.rest import Client

class TwilioNotifier:

    def __init__(self, conf):
        self.conf = conf

    def send(self, msg):
        client = Client(self.conf["twilio_sid"], self.conf["twilio_auth"])
        client.messages.create(to=self.client["twilio_to"],from_=self.conf["twilio_from"],body=msg)
