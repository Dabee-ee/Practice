# 혼자 공부하는 파이썬 53강 - 외부 모듈(프레임워크)


# flask github 예시 실행해보기

from flask import Flask         # Flask -> 캐멀케이스 = 클래스
app = Flask(__name__)           # 클래스를 사용해서 객체를 만든 뒤에, app이라는 변수에 집어 넣는 코드이다.

@app.route("/")                 # 데코레이터
def hello():
    return "Hello, World!"

# 파일 실행하는 방법
# set FLASK_APP=파일 이름.py        -> 환경 변수를 설정하는 부분. (FLASK_APP이라는 변수에다가 무언가를 넣는 코드)
# flask run                         -> FLASK 명령 (PIP 인스톨 할 때 같이 설치됨.)

