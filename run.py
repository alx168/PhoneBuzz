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
        #print(request.data.decode('ascii'))
        #print("form")
        if 'Digits' in request.form:
            digits = request.form['Digits']
           # gather.say(digits) 
            for i in range(1,int(digits)+1):
                if i % 3 == 0 and i % 5 == 0:
                    gather.say("FizzBuzz")
                elif i % 3 == 0:
                    gather.say("Fizz")
                elif i % 5 == 0:
                    gather.say("Buzz")
                else:
                    gather.say(str(i))
        else:
            gather.say("Hello, please enter a number to play fizzbuzz over the phone. Press # when you're done")    
        
        resp.append(gather)
    return str(resp)

if __name__ == "__main__":
    #bind to port if defined otherwise default to 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port);
