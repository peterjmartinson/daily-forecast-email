import requests
from bs4 import BeautifulSoup

# query = "covid".split()
# query_separator = "%20".join(query)

# start = "https://news.google.com/search?q="
# end = "&hl=en-IN&gl=IN&ceid=IN%3Aen"
# URL = start + query_separator + end

# r = requests.get(URL)
# soup = BeautifulSoup(r.content, 'html.parser')
# headlines = soup.find_all('a', class_='DY5T1d RZIKme')
# for i in headlines:
    # print(i.text)


base_url = 'https://forecast.weather.gov/product.php'
site = 'PHI'
query_string = '?site=' + site + '&issuedby=' + site + '&product=AFD&format=TXT&version=1&glossary=0'
url = base_url + query_string

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')
discussion = soup.find_all('pre', class_='glossaryProduct')
for i in discussion:
    print(i.text)
