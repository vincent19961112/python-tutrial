import json
import urllib.request as req
url = "https://www.dcard.tw/service/api/v2/forums/stayhome/posts?limit=100"
request = req.Request(url, headers={
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
})
print(request)
with req.urlopen(request) as response:
    data = response.read().decode("utf-8")


data = json.loads(data)
for item in data:
    print(item["title"])
