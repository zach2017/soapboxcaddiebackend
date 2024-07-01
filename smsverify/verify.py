import os
import azure.functions as func
from twilio.rest import Client

def main(req: func.HttpRequest) -> func.HttpResponse:
    # Get the phone number and verification code from the request
    phone_number = req.params.get('phone_number')
    verification_code = req.params.get('verification_code')

    # Validate the request parameters
    if not phone_number or not verification_code:
        return func.HttpResponse("Phone number and verification code are required.", status_code=400)

    # Twilio account credentials
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    verify_service_sid = os.environ['TWILIO_VERIFY_SERVICE_SID']

    # Create a Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Verify the phone number with the verification code
        verification_check = client.verify \
            .services(verify_service_sid) \
            .verification_checks \
            .create(to=phone_number, code=verification_code)

        # Check the verification status
        if verification_check.status == 'approved':
            return func.HttpResponse("Phone number verification successful.")
        else:
            return func.HttpResponse("Phone number verification failed.", status_code=400)

    except Exception as e:
        return func.HttpResponse(f"An error occurred: {str(e)}", status_code=500)