
import requests

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


URL = "http://www.casemario.com/goods/goods_list.php?cateCd=001"

def extract_image():
  images = []
  html = urlopen(URL).read()
  soup = BeautifulSoup(html, "html.parser")
  image = soup.find_all("img", {"class":"middle"})
  images = image
  return(images)

img = extract_image()

n = 1
for i in extract_image():
  imgurl = i["src"]
  with urlopen(imgurl) as f:
    with open("mario" + str(n) + '.gif', 'wb' ) as h:
      img = f.read()
      h.write(extract_image())
n += 1


