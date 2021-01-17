
import requests
from bs4 import BeautifulSoup


URL = "http://www.casemario.com/goods/goods_list.php?cateCd=001"

def extract_image():
  images = []
  result = requests.get(URL)
  soup = BeautifulSoup(result.text, "html.parser")
  image = soup.find_all("img", {"class":"middle"})
  images = image
  return(images)

print(extract_image())