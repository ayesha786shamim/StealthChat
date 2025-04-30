from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Twilio credentials and phone numbers
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("TO_PHONE_NUMBER")

# Initialize Twilio client
client = Client(account_sid, auth_token)

# Message content
custom_message = "###### Any Message You want to send ######"

# Send WhatsApp message
message = client.messages.create(
    from_=twilio_number,
    body=custom_message,
    to=to_number
)

# Print confirmation
print("✅ Message sent! SID:", message.sid)
