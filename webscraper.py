import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#enter url of site you want to scrape
url = ''
response = requests.get(url)
# if request is successful: response 200 displayed else troubleshoot

soup = BeautifulSoup(response.text, 'html.parser')
# retrieve all link elements and print out as strings 
for link in soup.findAll('a'):
  print link.string
