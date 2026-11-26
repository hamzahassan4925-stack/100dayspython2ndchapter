import requests
from bs4 import BeautifulSoup

url = "https://www.olx.com.pk/bahawalpur_g4060653/cats_c138" 

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 1. Webpage ka HTML fetch karna
response = requests.get(url, headers=headers, timeout=10)  # Agar 404/500 jaisa error ho to yahin bata dega

# 2. HTML ko parse karna
soup = BeautifulSoup(response.text, "html.parser")

# 3. Specific elements nikalna (apni zaroorat ke mutabiq selector badlein)
title = soup.find("h1")
print("Main Heading:", title.get_text(strip=True) if title else "N/A")

for link in soup.select("a"):
    href = link.get("href")
    text = link.get_text(strip=True)
    if href:
        print(f"Link: {text} -> {href}")