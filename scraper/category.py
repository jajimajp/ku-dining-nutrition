import requests
import re
from bs4 import BeautifulSoup

page = requests.get("https://www.u-coop.net/food/menu/hanshin/info.php")

soup = BeautifulSoup(page.content, 'html.parser')
nav = soup.find(id='main-navigation')
atags = nav.find_all('a')
for a in atags:
  href = a['href']
  pattern = re.compile(r'\?category=([0-9]*)')
  cap = pattern.search(href)
  category_id = cap.group(1)
  img = a.contents[0]
  assert img.name == 'img'
  alt = img['alt']
  print(category_id, alt)

