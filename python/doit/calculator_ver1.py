# n배수 찾아내기
for i in range(100):
    if i % 7 == 0: 
        print(i)

# 결과 값을 리스트로 출력되게 하는 방법이 궁금해짐.

# test1
a = []
for i in range(100):
    if i % 7 == 0: 
        print(a)

# test2        
for i in range(100):
    if i % 7 == 0: 
        print([i])

# test3
for i in range(100):
    if i % 7 == 0: 
        new_list = i
        print(new_list)

# test4 (21-01-12)
a = []
while range(100):
    if i % 7 == 0: 
        i = 0
        a += i
        print(a)


# 빈 리스트를 가지고 있는 변수를 만들어야 하나?