# 교집합을 만들어보자

v1 = set([1, 2, 3, 4, 5, 6])
v2 = set([4, 5, 6, 7, 8, 9])

print(v1 & v2)

print(v1.intersection(v2))

# 합집합을 만들어보자

print(v1 | v2)
print(v1.union(v2))

# 차집합을 만들어보자 

print(v1 - v2)
print(v1.difference(v2))

# 값 1개 추가하기 add

s1 = set([1, 2, 3, 4])
s1.add(7)

print(s1)

# 값 여러개 추가하기 update

s2 = set([1, 2, 3, 4,])
s2.update([5, 6, 7, 8 ,9])         # add는 소괄호 update는 중괄호까지.
print(s2)

# 그러면 여기에 중복된 값이 있다면?!   ->  당연히 집합이니까 중복된 값은 없어진다.

s3 = set([1, 2, 3, 4])
s3.update([1, 2, 5, 6, 7, 8, 9])
print(s3)


# 지워보자 remove

s4 = set([1, 2, 3])
s4.remove(1)
print(s4)

# 자료형. 불 (숫자, 문자와 비슷 / true & false)
# 언제 쓰이냐 ? if true / if false  -> print      or while true / while false   -> print

a = True
print(a)
print(type(a))

# 파이썬에서 어떤 상황에서 자료형이 참과 거짓을 가지는 지에 대해서도 알아야 한다. 
# 그 예로, 문자형에서 "python"과 같이 문자를 가지고 있다면 true, ""와 같이 문자를 가지고 있지 않다면 false로 판단한다.
# 예2)   숫자 1이 참, 0은 거짓, none은 거짓

a = "안녕"
if a :
    print(a)

# 반면에 값이 없다면

b = ""
if b :
    print(b)

# 출력이 되지 않는다.

c = [1, 2, 3, 4]
while c :
    c.pop()      # pop 마지막 요소를 꺼내 버리고 없앤다.
    print(c)     # True 값이면 반복 출력. 값이 안나올 때까지 요소들을 빼버린다. (값이 없어지면 false가 되니까)

# pop이 없다면 값을 무한정 찍어낸다.

# 변수를 알아보자. 
# a = 1 이 파이썬에서 가지는 의미는 a와 1이 같은 값이라는 수학적 의미가 아니라, 
# 오른쪽에 있는 1을 왼쪽 a라는 상자에 넣는다는 것이다. 
# (궁금증) a = ? 이라는 정의를 여러번 해주면 최종적으로 a라는 상자에 값들이 모두 들어있을까?

e1 = 1
e1 = 2
e1 = 3
print(e1)

# 가장 마지막에 쓴 값으로 프린트 된다. 그럼 모든 값을 다 넣어주는 방법에는 뭐가 있을까?

e2 = [1]
e2 = [2]
print(e2)

# add나 update 밖에 없나...?


# 새로운 상자에 이전 상자를 넣는 것은 가능할까?

e3 = [e1, e2, 5, 6, 7]
print(e3)                       # 가능!

# python tutor를 이용하면 시각적으로 확인할 수 있다.

print(e2 + [1, 2, 3])



# 리스트 변수 주의사항
a = [1, 2, 3]
b = a
a[1] = 4
print(a)
print(b)       
# 상자는 값의 주소를 가지고 있는 것이다. 
# 그러니 a의 리스트를 가지고 있는 b는 a라는 값을 복사해서 가져온게 아니고 
# a의 주소를 대신 보여주는 것이므로 변경된 a값을 출력한다.

# 주소값을 확인하면 같은 a와 b가 같은 곳을 바라보고 있다는 것을 알 수 있다.

print(id(a))
print(id(b))

print(a is b)   # 같은 값을 바라보고 있니? 라는 질문


# 그러면 복사는 어떻게 하는가?  (a값이 변경되어도 처음 가져온 a의 값이 유지되게 하는 방법)

c = [1, 2, 3, 4]
d = c[ : ]    # 슬라이싱

c[1] = 6
print(c)
print(d)   

print(id(c))
print(id(d))    # 주소도 달라졌다.

# 복사 방법 2

from copy import copy
o1 = [1, 2, 3]
o2 = copy(o1)
o1[1] = 5

print(o1)
print(o2)

print(id(o1))
print(id(o2))     # 슬라이싱을 했던 것과 같은 결과가 나온다.






# 변수를 할당하는 여러가지 방법을 알아보자.

z1, z2 = ('python', 'life')

print(z1)
print(z2)

(z1, z2) = ('python', 'life')

print(z1)
print(z2)    # 튜플을 이용해도 똑같음.

[z3, z4] = ('my name', 'dabee')

print(z3)
print(z4)     # 리스트를 이용

z5 = z6 = 'hello'

print(z5)
print(z6)   # 같은 값을 할당

# 변수끼리 값을 교환할 수 있다.

z7 = 3
z8 = 5

tmp = z8    # tmp라는 임시 저장소에 z8을 옮겨두자
z8 = z7
z7 = tmp

print(z7)
print(z8)

# tmp라는 임시변수에 하나씩 덮어쓰는 것

# tmp 없이 등호로만 교환 할 수는 없는가?

x1 = 7
x2 = 8

x1 = x2

print(x1)
print(x2)     # 안되고 x1이 x2로 변경된다.

# 등호를 쓰면 덮어쓰기 때문에 위의 식은 안되고 콤마를 이용하면 값을 교환할 수 있다.
x3 = 7
x4 = 8

(x3, x4) = (x4, x3)
print(x3)
print(x4) 




















