# Download the helper library from https://www.twilio.com/docs/python/install
import os
import sys
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
service_sid = os.environ["TWILIO_SERVICE_SID"]
phone = '+1' + sys.argv[1]

client = Client(account_sid, auth_token)

verification = client.verify.v2.services(
    service_sid
).verifications.create(to=phone, channel="sms")

print(verification.sid)