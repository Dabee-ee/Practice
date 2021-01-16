# 리스트 내포 예제


# i for i in range()
# 반복문을 매개변수에 입력된 값만큼 돌리는데, i를 요소로 사용해달라는 의미의 구문이다.

array_1 = [i for i in range(10)]
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
array_2 = [i for i in range(0, 10, 2)]
# 0, 2, 4, 6, 8
array_3 = [1 for i in range(10)]
# ?

print(array_1)
print(array_2)
print(array_3)

# 리스트 내포와 조건문
# 리스트 내포는 뒤에 조건문을 추가할 수도 있다.

array_4 = [i for i in range(10) if i % 2 == 0]
print(array_4)
