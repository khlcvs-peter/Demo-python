#爬蟲程式 抓ptt movies  view-source:https://www.ptt.cc/bbs/movie/index.html
import urllib.request as req
#url = "https://www.ptt.cc/bbs/movie/index.html"
url = "https://pttgame.com/"
request= req.Request(url,headers={
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response :
    data = response.read().decode("utf-8")
   # print(data)
import bs4
root = bs4.BeautifulSoup(data,"html.parser")
#print(root)
titles = root.find_all("span", class_="block-item-title")
#print(titles)
for title in titles :
    print(title.a.string)

