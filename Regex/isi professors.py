from bs4 import BeautifulSoup
import requests
import re

source = requests.get('https://www.isid.ac.in/~epu/faculty.html').text
soup = BeautifulSoup(source,'lxml')
