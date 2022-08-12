
import pytest
import datetime
import unittest.mock
from unittest.mock import patch

from aeolus import Aeolus

@pytest.fixture
def mock_emailer():
    with patch('builtins.input', side_effect=['Test Email', 'Test Password']) as mock_input:
        emailer = unittest.mock.MagicMock(name='emailer')
        emailer.sendEmail.return_value = True
        return emailer

class TestCanary:
    
    def test__chirp(self):
        assert 1 == 1




class TestAeolus_sendEmail:

    def test__sendWeatherEmail(self):
        pass
