import requests
import re
from bs4 import BeautifulSoup

def get_menu(url: str):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, features="lxml")
  divs = soup.find_all(class_="catMenu")
  for d in divs:
    print(d.prettify())

get_menu("https://west2-univ.jp/sp/menu.php?t=650111")