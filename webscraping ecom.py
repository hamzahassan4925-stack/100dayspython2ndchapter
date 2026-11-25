import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.com/s?k=iphone&rh=p_n_g-1003517064111%3A69690504011&dc&ds=v1%3Afu1walfjpxe92MQpvdkb6iORM5MCJOY9nw3dBjyA%2BEg&crid=34RLQNST2ANZ1&qid=1795608144&rnid=36816607011&sprefix=iphon%2Caps%2C353&ref=sr_nr_p_n_g-1003517064111_1"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.text, "html.parser")

spans = soup.select("div.sg-col-inner")
print("Status:", r.status_code)
print("Blocked / Captcha:", "captcha" in r.text.lower() or "robot" in r.text.lower())
print("Items found:", len(spans))
for item in spans[:3]:
    text = item.get_text(" ", strip=True)
    if text:
        print(text[:120])
        print("-" * 40)
for item in spans:
    title_el = item.select_one("h2")
    price_el = item.select_one(".a-price-whole")

    if title_el:
        title = title_el.get_text(" ", strip=True)
        price = price_el.get_text(strip=True) if price_el else "N/A"
        print(f"Title: {title}")
        print(f"Price: {price}")
        print("-" * 40)