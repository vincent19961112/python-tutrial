import urllib.request as req

def getData(url):
	request=req.Request(url, headers={
		"cookie": "_ga=GA1.2.1047959666.1620274980; __cf_bm=6a91e3928e2aba662ee1f28d18eb0269e2929e70-1625655365-1800-ASc9GIkE0C4PgFZ2hl4Ney3DwvMGdol3gUT3bRP3dZQuiufaJTp+mkIG7DQ3wOD0NejsvvpYlUYDr9XWdGhBqfo=; _gid=GA1.2.1773714880.1625655365; over18=1",
		"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
		})

	with req.urlopen(request) as response:
		data=response.read().decode("utf-8")

	import bs4
	root=bs4.BeautifulSoup(data,"html.parser")
	titles=root.find_all("div",class_="title")
	for title in titles:
		if title.a != None:
			print(title.a.string)
	nextLink=root.find("a",string="‹ 上頁")
	return nextLink["href"]

pageURL="https://www.ptt.cc/bbs/Gossiping/index.html"

count=0
while count < 10:
	pageURL ="https://www.ptt.cc" + getData(pageURL)
	count+=1
