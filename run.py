import os
from flask import abort, Flask, request
#from functools import wraps
from twilio.twiml.voice_response import Gather, VoiceResponse, Redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def hello():
    """responding to requests incoming"""
    resp = VoiceResponse()
    if (request.method =='GET' or request.method == 'POST'):
        gather = Gather()
        gather.say("Hello, please enter a number to play fizzbuzz over the phone. Press # when you're done")    
        #print(request.data.decode('ascii'))
        #print("form")
        digits = request.form['Digits']
        gather.say(digits) 
        resp.append(gather)
    
    return str(resp)

if __name__ == "__main__":
    #bind to port if defined otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port);
