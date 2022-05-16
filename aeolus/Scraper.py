import requests
from bs4 import BeautifulSoup

class Scraper:

    def __init__(self):
        pass

    def getWeatherForecast(self):
        base_url = 'https://forecast.weather.gov/product.php'
        site = 'PHI'
        query_string = '?site=' + site + '&issuedby=' + site + '&product=AFD&format=TXT&version=1&glossary=0'
        url = base_url + query_string
        forecast = url
        return forecast

    def getResponse(self, url):
        response = requests.get(url)
        return response

# base_url = 'https://forecast.weather.gov/product.php'
# site = 'PHI'
# query_string = '?site=' + site + '&issuedby=' + site + '&product=AFD&format=TXT&version=1&glossary=0'
# url = base_url + query_string

# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
# discussion = soup.find_all('pre', class_='glossaryProduct')
# for i in discussion:
#     print(i.text)
