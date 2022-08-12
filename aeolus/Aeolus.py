
import datetime
from email.message import EmailMessage

from aeolus import Emailer


class Aeolus:

    def __init__(self, emailer=None):
        self.emailer = emailer or Emailer.Emailer()

    def sendWeatherEmail(self, recipient='peter.j.martinson@gmail.com'):
        pass
