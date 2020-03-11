# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC8bc4edc04eef189b07e668c05b1787af'
auth_token = 'ea41b7b74338c411956a2e8628a1608f'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Bro usiogope sana its nathan here natest django sms....mambo ni fireeee.",
                     from_='+17244924842',
                     to='+255653140801'
                 )

print(message.sid)
