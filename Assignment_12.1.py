import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL Certification error
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url- ' )
count = int(input('Enter Count- '))
position = int(input('Enter Position- '))

for i in range(count):

    html = urllib.request.urlopen(url, context = ctx).read()
    soup  = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    url = tags[position - 1].get('href', None)
    print("Retrieving - ", url)
