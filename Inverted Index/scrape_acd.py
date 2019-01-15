import requests
import urllib.request
import time
from bs4 import BeautifulSoup

url = 'http://textfiles.com/etext/AUTHORS/DOYLE/'
response = requests.get(url)

soup = BeautifulSoup(response.text,'html.parser')
soup.find_all('a')

for i in range(len(soup.find_all('a'))):
    print(i+1)
    one_a_tag = soup.find_all('a')[i]
    link = one_a_tag['href']
    download_url = 'http://textfiles.com/etext/AUTHORS/DOYLE/'+link
    urllib.request.urlretrieve(url=download_url,filename=link)
    time.sleep(0.5)