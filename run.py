from flask import Flask
from twilio.twiml.voice_response import VoiceResponse

application = Flask(__name__)

@application.route("/", methods=['GET', 'POST'])

def hello():
    """responding to requests incoming"""
    resp = VoiceResponse()
    resp.say("Hello World!!!!")
    
    return str(resp)

if __name__ == "__main__":
    application.run(debug=True);
