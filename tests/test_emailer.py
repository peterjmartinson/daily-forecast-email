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

    @patch('builtins.input', side_effect=['Test Email', 'Test Password'])
    @patch('aeolus.Emailer.smtplib')
    @patch('aeolus.Emailer.ssl')
    def test__returns_a_subject(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        result = emailer.createOutgoingMessage()
        assert 'Subject' in result.keys()

    @patch('builtins.input', side_effect=['Test Email', 'Test Password'])
    @patch('aeolus.Emailer.smtplib')
    @patch('aeolus.Emailer.ssl')
    def test__returns_a_recipient(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        result = emailer.createOutgoingMessage()
        assert 'To' in result.keys()

    @patch('builtins.input', side_effect=['Test Email', 'Test Password'])
    @patch('aeolus.Emailer.smtplib')
    @patch('aeolus.Emailer.ssl')
    def test__returns_a_body(self, mock_ssl, mock_smtplib, mock_input):
        emailer = Emailer.Emailer()
        result = emailer.createOutgoingMessage()
        assert result.get_content()[:10] == 'Empty Body'



    # @patch('hermes.Hermes.Hermes.getFileInfo')
    # def test__returns_a_message(self, patched_method, mock_emailer, mock_conn, new_file_info):
    #     db_handler = EDWAccess.EDWAccess(connection=mock_conn)
    #     hermes = Hermes.Hermes(emailer=mock_emailer, db_handler=db_handler)
    #     test_file_info = new_file_info
    #     test_file_id = test_file_info['FileID']
    #     patched_method.return_value = test_file_info
    #     result = hermes.createOutgoingMessage(test_file_id)
    #     assert result.get_content()[:10] == 'Greetings,'






