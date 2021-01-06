import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = 0

url = input('Enter_Location: ')
print ("===== retrieving URL. =====")
uh = urllib.request.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
    #print item["count"]
    number = int(item["count"])
    count = count + number
print (count)
