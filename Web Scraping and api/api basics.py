from bs4 import BeautifulSoup
import lxml
import requests
import re

source = requests.get('https://coreyms.com/').text
soup = BeautifulSoup(source,'lxml')
article = soup.find('article')

# headline = article.h2.a.text
# #print(headline)
# print(link.prettify())

link = soup.find('iframe',class_ = 'youtube-player')['src']
ytlink = re.findall('embed/(.+)\?',link)
print(link,ytlink)