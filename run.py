import os
from flask import abort, Flask, request
#from functools import wraps
from twilio.twiml.voice_response import Gather, VoiceResponse, Redirect

application = Flask(__name__)

@application.route('/hello', methods=['GET', 'POST'])

def hello():
    """responding to requests incoming"""
    resp = VoiceResponse()
    gather = resonse.gather()
    gather.say("Hello, please enter a number to play fizzbuzz over the phone. Press # when you're done")
    digits = request.form['Digits']
    gather.say(digits) 
    
    #if user enters nothing
    #resp.redirect('./hello')
    
    return str(resp)

if __name__ == "__main__":
    #bind to port if defined otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    application.run(host='0.0.0.0', port=port);
