import json
import urllib.request as req
year = str(2020)
mount = str(12)
url = "https://www.google.com/doodles/json/" + year + "/" + mount + "?hl=en"

request = req.Request(url, headers={
    "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",
    "content-type": "application/json;charset=utf-8",
})
with req.urlopen(request) as response:
    data = response.read().decode('utf-8')

data = json.loads(data)

for d in data:
    url = "https:"+d['url']
    fname = "doodles" + url.split("/")[-1]
    response = req.urlopen(url)
    img = response.read()

    f = open(fname, "wb")
    f.write(img)
    f.close()
