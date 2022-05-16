import pytest
import unittest.mock
from unittest.mock import patch

from aeolus import Emailer


@pytest.fixture
def mock_conn():
    mock_connection = unittest.mock.MagicMock(name='mock_conn')
    mock_connection.cursor.return_value.fetchall.return_value = [(1, ), (2, ), (3, )]
    return mock_connection

class TestCanary:
    
    def test_it_chirps(self):
        assert 1 == 1
        

class TestEmailer:

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

