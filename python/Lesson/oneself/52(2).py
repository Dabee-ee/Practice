# 혼자 공부하는 파이썬 52강 - 외부 모듈(라이브러리)

# 모듈과 모듈을 조합해서 더 큰 가치를 만들어낼 수 있다.

from urllib import request
from bs4 import BeautifulSoup

content = request.urlopen("http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=4155025000")   
# urlopen 으로 자료를 긁어올 웹사이트를 열어주자.
soup = BeautifulSoup(content, 'html.parser')        
# content를 바로 Beautiful Soup으로 읽어들인다.

for data in soup.select("data"):
    print("시간: ", data.select_one("hour").string)        
    print("날씨: ", data.select_one("wfkor").string)
# data자료에 soup.select를 사용했던 것과 같이 data.select를 사용해서 필요한 녀석들을 가져오면 된다.
    print("-" * 20)     # data를 구분하기 위해 구분선을 만들어줌.



