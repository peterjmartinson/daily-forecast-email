import pytest
import unittest.mock
from unittest.mock import patch

from aeolus import Emailer


class TestCanary:
    
    def test_chirp(self):
        assert 1 == 1
        

class TestEmailer_sendEmail:

    @patch('builtins.input', side_effect=['Test Email', 'Test Password'])
    @patch('aeolus.Emailer.smtplib')
    @patch('aeolus.Emailer.ssl')
    def test__sendEmail_calls_login(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        mock_ssl.return_value.create_default_context.return_value = 'Test Context'
        test_email = 'Test Email'
        test_password = 'Test Password'
        test_message = {'message': 'Test Message'}
        emailer.sendEmail(test_message)
        print('CALLS:  ', mock_smtplib.SMTP_SSL.return_value.__enter__.return_value.mock_calls)
        mock_smtplib.SMTP_SSL.return_value.__enter__.return_value.login.assert_called_with(test_email, test_password)

class TestEmailer_createOutgoingMessage:

    @patch('builtins.input', side_effect=['Test Email', 'Test Password']) # processes two fake inputs
    @patch('aeolus.Emailer.smtplib') # mocks out the SMTP library
    @patch('aeolus.Emailer.ssl') # mocks out SSL calls
    def test__returns_a_dummy_subject(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        result = emailer.createOutgoingMessage()
        assert 'Subject' in result.keys()

    @patch('builtins.input', side_effect=['Test Email', 'Test Password']) # processes two fake inputs
    @patch('aeolus.Emailer.smtplib') # mocks out the SMTP library
    @patch('aeolus.Emailer.ssl') # mocks out SSL calls
    def test__returns_a_subject(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        test_subject = 'test subject'
        result = emailer.createOutgoingMessage(subject=test_subject)
        assert result['Subject'] == test_subject

    @patch('builtins.input', side_effect=['Test Email', 'Test Password'])
    @patch('aeolus.Emailer.smtplib')
    @patch('aeolus.Emailer.ssl')
    def test__returns_a_dummy_recipient(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        result = emailer.createOutgoingMessage()
        assert 'To' in result.keys()

    @patch('builtins.input', side_effect=['Test Email', 'Test Password'])
    @patch('aeolus.Emailer.smtplib')
    @patch('aeolus.Emailer.ssl')
    def test__returns_a_recipient(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        test_recipient = 'test recipient'
        result = emailer.createOutgoingMessage(recipient=test_recipient)
        testresult = emailer.createOutgoingMessage()
        assert result['To'] == '"test recipient"'

    @patch('builtins.input', side_effect=['Test Email', 'Test Password'])
    @patch('aeolus.Emailer.smtplib')
    @patch('aeolus.Emailer.ssl')
    def test__returns_a_body(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        result = emailer.createOutgoingMessage()
        assert result.get_content() == 'Empty Body\n'



