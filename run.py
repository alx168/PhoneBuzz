import os
from flask import Flask
from twilio.twiml.voice_response import Gather, VoiceResponse

application = Flask(__name__)

@application.route("/", methods=['GET', 'POST'])

def hello():
    """responding to requests incoming"""
    resp = VoiceResponse()
    resp.say("Hello, please enter a number to play fizzbuzz over the phone.  ")
    resp.say("Press # when you're done.")
    gather = Gather()
    resp.say("you entered: ")
    resp.append(gather)
    
    
    return str(resp)

if __name__ == "__main__":
    #bind to port if defined otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port);
