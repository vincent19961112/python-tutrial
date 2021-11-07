import urllib.request as req
url="https://www.google.com/search?tbm=vid&sxsrf=ALeKk01kotSDoAP5RGdUsMj-LFa-T5bjag:1624860261974&q=%E7%B7%9A%E6%80%A7%E4%BB%A3%E6%95%B8&sa=X&ved=2ahUKEwiIv-WV1LnxAhUQwosBHQpRCH0Q8ccDegQIBxAD&biw=1745&bih=852"
request=req.Request(url, headers={
	"user-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
	})
with req.urlopen(request) as response:
	data=response.read().decode("utf-8")

import bs4
root=bs4.BeautifulSoup(data,"html.parser")
titles=root.find_all("h3")
for title in titles:
	print(title.string)
