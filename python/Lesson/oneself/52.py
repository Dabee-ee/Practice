# 혼자 공부하는 파이썬 52강 - 외부 모듈(라이브러리)

html_doc = """
<html>
    <head>
        <title>TEST PAGE</title>
    </head>
    <body>
    <h1>HELLO WORLD</h1>
    </body>   
</html>
"""

# 예제에서 그대로 가져와 사용해도 된다.
from bs4 import BeautifulSoup          
soup = BeautifulSoup(html_doc, 'html.parser')
# html_doc을  html.parser라는 것으로 읽어들여서 soup이라는 객체로 변환을 해준다.      

print(soup.select("h1"))   
# soup에서 select 라는 녀석을 굉장히 많이 사용함. 
# h1이라는 녀석을 select로 잡고 출력한다는 의미의 코드.
print(soup.select("h1")[0].string)   
# h1의 스트링을 출력.          
# .string이라는 속성은 Beautigul Soup이 제공해주는 기능.


