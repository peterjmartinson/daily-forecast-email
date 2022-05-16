
import pytest
import datetime
import unittest.mock
from unittest.mock import patch

from aeolus import Scraper


@pytest.fixture
def mock_requests():
    mock_requests = unittest.mock.MagicMock(name='mock_requests')
    mock_requests.get.return_value = 'some html'
    return mock_requests


class TestCanary:
    
    def test_it_chirps(self):
        assert 1 == 1

class TestScraper_getWeatherForecast:
    
    def test__returns_string(self):
        scraper = Scraper.Scraper()
        result = scraper.getWeatherForecast()
        assert type(result) is str

class TestScraper_getResponse:
    
    @patch('aeolus.Scraper.requests')
    def test__returns_content(self, patch_requests):
        scraper = Scraper.Scraper()
        patch_requests.get.return_value.content.return_value = 'some response'
        url = 'test url'
        result = scraper.getResponse(url)
        # print(patch_method.return_value.call_list)
        assert result.content.return_value == 'some response'
