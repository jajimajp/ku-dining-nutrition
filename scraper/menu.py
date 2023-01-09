import requests
import re
from bs4 import BeautifulSoup

# get menu categories
def get_menu_categories(url: str):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, features="lxml")
  divs = soup.find_all(class_="catMenu")
  for d in divs:
    print(d.prettify())

def get_menu(url: str):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, features="lxml")
  h3s = soup.find_all("h3")
  ret = []
  for i in h3s:
    ret.append(i.get_text())
  return ret

if __name__ == "__main__":
  syokudou = "中央食堂"
  with open("./tmp/menu_chuou.txt") as f:
    menu_str = f.read()
  menu_base = "https://west2-univ.jp/sp/"
  lines = menu_str.split("\n")
  menus = []
  for l in lines:
    cols = l.split(",")
    # Name, url_postfix
    if len(cols) < 2:
      continue
    menus.append((cols[0], cols[1]))
  
  # print menus in markdown format
  print(f"# {syokudou}")
  print("")
  for (n, u) in menus:
    url = f"{menu_base}/{u}"
    m = get_menu(url)
    print(f"## {n}")
    print("")
    for i in m:
      print(f"- {i}")
    print("")
