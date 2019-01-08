import urllib.request
import json
wp = urllib.request.urlopen("http://localhost:3000/api/categories?page=1&per_page=10")
pw = wp.read()
js = json.loads(pw)
print(js['categories'])

for i in js['categories']:
    print(i['name'])

