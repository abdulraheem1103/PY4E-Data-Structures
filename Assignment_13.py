import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET 
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter Location: ')

result = 0 
print('Retrieving', url)
ls = urllib.request.urlopen(url, context=ctx)

data = ls.read()
tree = ET.fromstring(data)


counts = tree.findall('.//count')
print("Count:", len(counts))
for count in counts:
    value = count.text
    result = result + int(value)

print("Sum - ", result)
