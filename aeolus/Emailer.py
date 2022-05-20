import ssl
import smtplib
from email.message import EmailMessage

class Emailer:

    sender_email = 'hermesdev41@gmail.com'
    password = None
    
    def __init__(self):
        print(f'Hermes email address:  {self.sender_email}')
        self.sender_email = input('Type your sender email and press enter:  ')
        self.password = input('Type your password and press enter:  ')

    def sendEmail(self, outgoing_message):
        port = 465  # For SSL
        context = ssl.create_default_context()
        outgoing_message['From'] = self.sender_email
        with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
            server.login(self.sender_email, self.password)
            server.send_message(outgoing_message)
        return True

    def createOutgoingMessage(self, subject='Subject', recipient='Recipient', message='Empty Body'):
        outgoing_message = EmailMessage()
        outgoing_message.set_content(message)
        outgoing_message['Subject'] = subject
        outgoing_message['To'] = recipient
        return outgoing_message



