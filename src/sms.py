# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(mensaje):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC926b5a2050c68868234a18cef47baa78'
    auth_token = 'ab09d55bfd162b5c5dfa05f5a624407d'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=mensaje,
                        from_='+12029328811',
                        to='+56991345693'
                    )

    print(message.sid)

send('hola')