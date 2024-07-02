import os
from twilio.rest import Client
from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
service_sid = os.environ["TWILIO_SERVICE_SID"]

@app.route('/getcode', methods=['GET'])
def code1():
    # Access form data
    phone = "+1" + request.args.get('phone')
    print(phone)
    
    try:
     client = Client(account_sid, auth_token)

     verification = client.verify.v2.services(service_sid).verifications.create(to=phone, channel="sms")

     print(verification.sid)
     return f"Received: Username: {phone}"
    except:
      return f"Error: *101*"

@app.route('/verify', methods=['GET'])
def submit_form():
    # Access form data
    phone = "+1" + request.args.get('phone')
    smscode = request.args.get('code', type=str)

    try:
      client = Client(account_sid, auth_token)

      verification_check = client.verify.v2.services(service_sid).verification_checks.create(to=phone, code=smscode)

      print(verification_check.status)

      return f"Received: Username: {phone}, status: {verification_check.status}"
    except:
      return f"Error: *101*"

if __name__ == '__main__':
    app.run(debug=True)