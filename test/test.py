from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa5389001a40cc135b22f613dbece6427"
# Your Auth Token from twilio.com/console
auth_token  = "ac7d74be2b212cb5b7f17bd9b17ea855"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+50378306221",
    from_="+15162102220 ", 
    body="Hello Ale")

print(message.sid)

