 We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

    Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
    Actual data: http://py4e-data.dr-chuck.net/comments_278052.html (Sum ends with 29)
    
  
 
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

content = []
total = 0

#ssl certification errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ('Enter - ')
html = urllib.request.urlopen(url, context = ctx).read()
soup = BeautifulSoup (html, 'html.parser')

#Retrieve all tags
tags = soup('span')
for tag in tags:
    content.append(tag.contents[0])

for i in range(len(content)):
    total = total + int(content[i])
    
print('Sum', total) #Sum is 2229
