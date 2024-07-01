
import os
import sys
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
service_sid = os.environ["TWILIO_SERVICE_SID"]
phone = '+1' + sys.argv[1]
smscode = sys.argv[2]

client = Client(account_sid, auth_token)

verification_check = client.verify.v2.services(
    service_sid
).verification_checks.create(to=phone, code=smscode)

print(verification_check.status)