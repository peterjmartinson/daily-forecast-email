
import datetime
from email.message import EmailMessage

from aeolus import Emailer


class Aeolus:

    def __init__(self, emailer=None):
        self.emailer = emailer or Emailer.Emailer()

    def createOutgoingMessage(self):
        outgoing_message = EmailMessage()
        outgoing_message['Subject'] = f'Subject'
        outgoing_message['To'] = f'Recipient'
        return outgoing_message
