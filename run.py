import os
from flask import abort, Flask, request
#from functools import wraps
from twilio.twiml.voice_response import Gather, VoiceResponse, Redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello():
    """responding to requests incoming"""
    resp = VoiceResponse()
    gather = Gather()
    gather.say("Hello, please enter a number to play fizzbuzz over the phone. Press # when you're done")
    resp.append(gather)
    #digits = request.values['Digits']
    if gather == 1:
        gather.say("goodbye");
    #gather.say(digits) 
    #resp.append(digits)
    #if user enters nothing
    #resp.redirect('./hello')
    
    return str(resp)

if __name__ == "__main__":
    #bind to port if defined otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port);
