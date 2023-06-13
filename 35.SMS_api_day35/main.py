# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC3dd3a8aa9579319c753aa5c8e569d42a"
auth_token = "a9f4588a0bd9ac0857ebcf3805e383d7"
client = Client(account_sid, auth_token)
message = client.messages.create(
  body="Hello from Twilio",
  from_="+14302455245",
  to="+918424882274"
)
print(message.sid)
