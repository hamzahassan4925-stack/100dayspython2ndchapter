import requests
from bs4 import BeautifulSoup

proxies = {
    "http": "http://customer-rcodewithharry:ActcitXccR8xbxs@pr.oxylabs.io:7777",
    "https": "http://customer-rcodewithharry:ActcitXccR8xbxs@pr.oxylabs.io:7777"
}

url = "https://www.amazon.com/Apple-Version-Orange-Unlocked-Renewed/dp/B0FTCDJHXR/ref=sr_1_2?crid=34RLQNST2ANZ1&dib=eyJ2IjoiMSJ9.UQZS5nYvBg5B3CdHJjBSc37ZjB80URzWSjlPoEH0hx657XkIXd9DrvgZF0iP-rlfKazay503viHVNu6W4-wW7683li8uPHPoeSaua8Dcatkww0cTteRQelN9nhbDfC0gysWg50-_HmJ63S7kOp4rSSB78sNHpg_pzrhSfCxrNQHu5fKAWzLNTUuuAu0HKTVOha9xnxyXIpfrG6ftxx5bamKJEHeA8sigm2wSWcFrt9Q.u6thSMKOLiqE1XNTmbUrXKGLM8W_nsSmC2JiAld3BIw&dib_tag=se&keywords=iphone&qid=1795607467&sprefix=iphon%2Caps%2C353&sr=8-2&th=1"

r = requests.get(url, proxies=proxies)
soup = BeautifulSoup(r.text, "html.parser")