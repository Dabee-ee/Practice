# 제어문 (조건문, 반복문)

# 조건문 (if문)
# 돈이 있으면 택시를 타고, 돈이 없으면 걸어 간다.

money = True
if money :        # money = true
    print("택시를 타고 가라")
else :              # false
    print("걸어가라")

# if문에는 비교연산자도 사용할 수 있다.
a = 1
b = 2

if a < b :
    print("확인")
else :
    print("미확인")

# == 같다, != 다르다
# >= 크거나 같다
# <= 작거나 같다

# if문을 활용하여 판단하기

stock = 1000 
if stock >= 2000 :
    print("사라")
else :
    print("사지마라")

# and, or, not
# and 둘 다 참이어야 한다.  ( & )
# or 둘 중에 하나라도 참이면 참  ( | )
# not 뒤에 값이 바뀐다? not false = true


# 찾고자 하는 값 in 리스트, 튜플 (자료)

if 1 in [1, 2, 3] :
    print("있음")
else :
    print("없음")

# not it

if 1 not in [1, 2, 3] :
    print("없음")
else :
    print("있음")

# 조건문에서 아무일도 하지 않게 설정하고 싶다면 'pass'

if 1 in [1, 2, 3] :
    pass
else : 
    print("없음")

# 조건이 여러개라면? 'elif'

pocket = ['papter', 'cellphone']
card = True
if 'money' in pocket :
    pass
elif card :
    print("택시를 타고 가라")
else :
    print("걸어가라")       

# test2

stock = ['삼성전자', 'LG전자']
SK = True
if '다비전자' in stock :            # false면 다음으로 넘어감. True 값이 나올 때 까지.
    pass
elif SK :
    print("없지만 사야 된다.")
else :
    print("사지마라")

# 만약 if 에서 참이 나오면 첫번째 if문의 값을 출력해주고, 그렇지 않으면 elif가 참일 경우의 값을 출력해준다.
# 우선순위별로 참 값을 찾아내서 가장 참인 값을 찾아내는 것?
# 결국 모두 false면 else의 값을 출력!


score = 70
if score >= 60 :
    message = "success"
else :
    message = "failure"
print(message)

# 위의 표현을 간단하게 하는 방법 '조건부 표현식'

score = 55
message = "successs" if score >=60 else "failure"   
print(message)






# 반복문 (while , for 문)
# 나무를 10번 찍는다. -> 10번을 찍으면 false가 되므로 작동을 멈춘다.
# 활용 ) 메일을 1000통을 보낸다, 코드를 여러번 짠다.


# while문의 기본 구조
# while <조건문> : \n   <수행할 문장1> \n   <수행할 문장2> ...


treeHit = 0
while treeHit < 10 :
    treeHit = treeHit + 1
    print("나무를 %d번 찍었습니다." % treeHit)
    if treeHit == 10 :
        print ("나무 넘어갑니다.")

# 위 조건문의 작동을 확인하려면 디버깅을 해보면 된다.


coffee = 10
money = 300

while money :     # 여기서 왜 자동으로 돈이 커피의 가격만큼 깎이는건지?
    print("돈을 받았으니 커피를 줍니다.")
    coffee = coffee - 1
    print("남은 커피의 양은 %d개 입니다." % coffee)
    if not coffee :
        print("커피가 다 떨어졌습니다. 판매를 중단합니다.")
        break

bread = 10
bm = 500

while bm :
    bread = bread - 1
    print("판매할 수 있는 빵의 양은 %d개 입니다." % bread)

    if not bread :
        break    # 중단하는 명령어를 써주지 않으면 무한 반복. break = 반복문을 빠져나간다.

# 단순히 판매할 수 있는 양을 출력하고 싶다면?

apple = 10
am = 500
box = am/apple

print("사과의 재고는 %d개 입니다." % box)


# continue

a = 0
while a < 10 :
    a = a + 1
    if a % 2 == 0 :
        continue            # if문이 참이 되면 while문의 처음으로 돌아가서 반복해라. 거짓이면 a값을 print해라.
    print(a)



# for문
# for 변수 in 리스트 (또는 튜플, 문자열) : \n   수행할 문장1 \n     수행할 문장2
# 이 때, 변수는 리스트에서 하나씩 꺼낸 값. 하나씩 담고 출력하는 걸 반복.

test_list = ['one', 'two', 'three']
for i in test_list :
    print(i)

# for 문의 활용

b = [(1, 2), (4, 5), (7, 8)]
for (first, last) in b :
    print(first)
    print(last)


c = [(1, 2), (4, 5), (7, 8)]
for (first, last) in c :
    print(first + last)


# 종합판

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks :
    number = number + 1
    if mark >= 60 :
        print("%d번 학생은 합격입니다." % number)
    else :
        print("%d번 학생은 불합격입니다." % number)

# 반복해서 검사하고 문장 출력하기.

# 합격생만 걸러내보기

marks1 = [90, 25, 67, 45, 80]
number1 = 0
for mark1 in marks1 :
    number1 = number1 + 1
    if mark1 >= 60 :
        print("%d번 학생은 합격입니다" % number1)
    else :
        pass

# for문과 continue

marks2 = [90, 25, 67, 45, 80]
number2 = 0
for mark2 in marks2 :
    number2 = number2 + 1
    if mark2 < 60 : continue
    print("%d번 학생은 합격입니다. 축하합니다." % number2)

# range

sum = 0
for i in range(1,11) :
    sum = sum + i
print(sum)

print(1+2+3+4+5+6+7+8+9+10)

# 한 차례씩 더하기를 반복.

# 구구단

goo = 10
for u in range(2,10) :
    for w in range(1,10) :
        print(u * w, end=" ")           # 안쪽 for문이 다 끝나야 바깥쪽 for문이 반복된다.
    print(' ')


# 리스트 내포
# result = [num * 3 for num in a if num % 2 == 0]
# result = []
# for num in a :
# if num % 2 == 0
# result.append(num * 3)
