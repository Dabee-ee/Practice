from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

Url = 'http://www.casemario.com/main/index.php' # 네이버 검색url
html = urlopen(url) # url 열기
soup = BeautifulSoup(html, "html.parser")
image = soup.find_all("div", {"class":"thumbnail"}).find("a")["img"]

n = 1
for i in img: # 이미지를 50개 저장하기 위한 반복문
    imgUrl = i['data-source'] 
    with urlopen(imgUrl) as f:
        with open('/goods/' + '.gif') as h: # 이미지 + 사진번호 + 확장자는 jpg
            img = f.read() #이미지 읽기
            h.write(img) # 이미지 저장
    n += 1
print('다운로드 완료')