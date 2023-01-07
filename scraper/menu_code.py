import requests
import re
from bs4 import BeautifulSoup

def get_menu(category_id, base_url="https://www.u-coop.net/food/menu/hanshin/info.php"):
  page = requests.get(f"{base_url}?category={category_id}")
  soup = BeautifulSoup(page.content, features="lxml")
  atags = soup.find_all("a")
  menus = []
  for i in atags:
    result = re.match(r".*\?menu_code=(\d+)\"", str(i))
    if result:
      name = str.strip(i.getText())
      menus.append((result.group(1), name))
  return menus

def get_menu_codes_for_all_categories():
  category_ids = [
    6101, # ごはん
    6102, # 丼・カレー
    6111, # 主菜
    6112, # 小鉢・汁物
    6121, # 麺類
    6142, # デザート
    6152, # テイクアウト
    6105, # セット・定食
  ]
  ret = []
  for id in category_ids:
    menus = get_menu(id)
    ret.extend(menus)
  return ret

if __name__ == '__main__':
  res = get_menu_codes_for_all_categories()
  for (code, name) in res:
    print(code, name, sep=',')