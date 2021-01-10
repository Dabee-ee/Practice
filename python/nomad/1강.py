# Lists in Python
# 많은 값을 한 곳에 저장하고 싶을 때 list를 사용

# ver.1 "Show me the days."
print("version_1 \n")

days_1 = ["Mon, Tue, Wed, Thur, Fri"]
print(days_1)


print("-" * 20)


# ver.2 "Tell me What the third day is."
print("version_2 \n")

days_2 = ["Mon", "Tue", "Wed", "Thur", "Fri"]
# "" 콤마 안에 묶인 문자가 하나의 자료가 된다.
# ver.1의 요일들을 각각의 요일로 구분지어 활용하기 위해 ""로 나누어 주었다.  



# list가 여러 자료들을 한 곳에 가지고 있으니, 
# 한 곳에서 다양한 정보를 추출하고 활용할 수 있어서 너무 유용하다. Good.
print(days_2)

print("Do you have 'Mon'?  ==>  ", "Mon" in days_2)
print("Do you have 'Man'?  ==>  ", "Man" in days_2)
# 게다가, 리스트에 연산자를 사용할 수도 있다.

print("Tell me what the third day is.  ==>  ", days_2[2])       # 컴퓨터는 카운트할 때 0부터 한다. 
print("How Many letters?  ==>  ", len(days_2))


print("-" * 20)


# ver.3 append 함수 활용
print("version_3 \n")

days_3 = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_3)

days_3.append("Sat")
print(days_3)
print(days_3)       
# dyas_3가 현재의 값을 유지하는지 궁금해서 한번 더 출력해보았다.
# append 함수를 사용하면 값이 영구적으로 변한다...


print("-" * 20)


# ver.4 reverse 함수 활용
print("version_4 \n")

days_4 = ["Mon", "Tue", "Wed", "Thur", "Fri"]
print(days_4)

days_4.append("Sat")
days_4.reverse()                     # 괄호 여닫기 필수
print(days_4)
print(days_4)
# 이번에도 값이 영구적으로 변했다.



# list가 없다면 
# day_one = "Mon"
# day_two = "Tue"  
# 위 처럼 같이 힘들게 코드를 작성해야 됐을 것이다... 끔찍.