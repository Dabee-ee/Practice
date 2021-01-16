# 혼자 공부하는 파이썬 29강 - 리스트와 딕셔너리에 적용하는 함수


# 딕셔너리로 쉽게 반복문 작성하기 : items()
# 기본 형태 for key, value in 리스트.items():
a = { "key_1" : "value_1", "key_2" : "value_2", "key_3" : "value_3" }
for key, value in a.items():
    print("{}키의 값은 {}입니다.".format(key, value))
