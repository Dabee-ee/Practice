# 함수 (입력과 출력은 어떻게 할까?)


# 입력과 출력이 없을 수도 있음.

# 파이썬 함수의 구조
# def 함수명(매개변수) \n <수행할 문장1> \n return 리턴 값

def sum(a, b) :
    result = a + b
    return result

# 위의 식을 사용하려면 '호출'을 해야됨

print(sum(1, 2))


# 입력과 출력이 없는 것

def say() :
    return 'Hi'

print(say())

def sum(c, d) :
    print("%d, %d의 합은 %d입니다." % (c, d, c+d))

sum(1, 2)
print(sum(1,2))    # 리턴 값이 없기 때문에 none이 나옴


# 출력 값이 있는지 없는지 확인해보자.

My_list = [1, 2, 3]
My_list.append(4)
print(My_list)

# but 

My_list2 = [1, 2, 3]
print(My_list2.append(4))           # I don't understand....  append는 리턴값이 없는 함수?

My_list3 = [1, 2, 3]
print(My_list3.pop())

# 어떤거는 print가 되고 어떤거는 print가 안되는 이유 => 함수의 특성에 따라?



# 여러 개의 인자를 한 번에 받는 방법 '*args'

def sum_many(*args) :
    sum = 0 
    for i in args :
        sum = sum + i
    return sum
print(sum_many(1,2,3))

# I don't understand.... too hard!

def print_kwargs(**kwargs) :
    for k in kwargs.keys() :
        if (k == "name") :
            print("당신의 이름은 :" + k)
print(print_kwargs(a="1", b="2"))



# 함수의 값은 언제나 하나이다.

def sum_and_mul(a, b) :
    return a+b, a*b

print(sum_and_mul(1,2))         # 더한 값과 곱한 값이 튜플 형태로 묶여서 '하나의 리턴값'으로 나온다.

# 여러 개의 값을 리턴하고 골라서 사용할 수 있다. print(sum_and_mul(1,2),[0]) 


def say_myself(name, old, man=True) :
    print("나의 이름은 %s 입니다." % name)
    print("나이는 %d 입니다." % old)
    if man :
        print("남자입니다.")
    else :
        print("여자입니다.")
say_myself("노다비",27,False)

# def say_myself2(name, old, man) :
#    print("나의 이름은 %s 입니다." % name)
#    print("나이는 %d 입니다." % old)
#    if man :
#        print("남자입니다.")
#    else :
#        print("여자입니다.")
# say_myself2("노다비",27)    

# 위의 오류 예제 처럼 기본값을 설정을 안해주거나,
# 순서대로 입출력 값을 맞춰주지 않으면 오류가 난다.
# 기본값은 입력을 안해줘도 출력이 되지만 순서가 맨 뒤로 가야된다. 중간에 기본값을 설정해놓으면 입력 안했을 경우에 오류가 난다.




# 함수 안에서 선언된 변수의 효력 범위

a = 1
def vartest(a) :
    a = a + 1

vartest(a)
print(a)

# a = 1 이니까 출력값이 2가 나와야 될 것 같은데 왜 1이 나오는 것인가?
# 함수 안에서 선언되는 변수는 그 함수의 안에서만 효력을 가지기 때문이다!


# 그러면 영향을 주려면 어떻게 하는가?
# 안쪽의 함수의 output을 만들어서 밖의 함수에서 다시 할당

b = 1
def vartest2(b) :
    b = b + 1
    return b

b = vartest2(b)
print(b)

# global 예약어도 사용 가능

c = 1
def vartest3() :
    global c
    c = c + 2

vartest3()
print(c)



# 'lambda' 함수를 간단하게 표현하는 방법

MyList = [lambda a, b : a + b, lambda a, b : a * b]

print(MyList[0](3,4))
print(MyList[1](3,4))

# 사용자 입력과 출력 input의 사용

# a = input("숫자를 입력하세요")
# print(a)

# 사정에 정의되어 있는 함수 = 내장함수
# def 사용자가 정의한 함수 = 사용자정의함수

# print문

print("Life is too short, You need python")

# 콤마를 넣으면 띄어쓰기가 되는 기능이 있다.



for i in range(10) :
    print(i, end=" ")


# 파일 읽고 쓰기

# w 읽기모드
# r 쓰기모드
# a 추가모드 - 파일의 마지막에 새로운 내용을 추가 시킬 때 사용

f = open("새파일.txt", 'w')     # 상대주소
f.close() 


f = open("C:/python/새파일.txt", 'w')     # 절대주소
for iu in range(1,11) :
    data = "%d번째 줄입니다. \n" % iu
    f.write(data)
f.close()

# readline

f = open("C:/python/새파일.txt", 'r')    
line = f.readline()
print(line)
f.close()

# 여러 줄을 읽으려면?

f = open("C:/python/새파일.txt", 'r')    
while True :
    line = f.readline()     # 라인이 있으면 계속 반복해서 출력해라.
    if not line : break     # 라인이 더 이상 없으면 멈춰라.
    print(line)
f.close()

# 모든 라인을 다 읽어오기. readlines

f = open("C:/python/새파일.txt", 'r')    
lines = f.readlines()
for line in lines :
    print(line)
f.close()

# read 
# readline은 한줄씩 읽어오는 것. 그래서 반복문을 써야함.
# readlines는 리스트 형태로 읽어오는 것.  그래서 for문을 쓰는 것.
# read는 통째로.

f = open("C:/python/새파일.txt", 'r')    
data = f.read()
print(data)
f.close()


# w - 새로 쓰는 것
# a - 추가 하는 것

f = open("C:/python/새파일.txt", 'a')    
for iu in range(11, 20) :
    data = "%d번째 줄입니다. \n" % iu
    f.write(data)
f.close()


f = open("C:/python/새파일.txt", 'r')    
data = f.read()
print(data)
f.close()


# with문과 함께 사용하기  - close를 굳이 안해도 됨.

with open("C:/python/foo.txt", "w") as f :
    f.write("Life is too short, you need python.")


