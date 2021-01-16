# 30강 문제풀어보기

# 2진수, 8진수, 16진수로 변환하는 코드는 많이 사용됩니다. 다음과 같은 형태로 10진수를 변환할 수 있습니다.

# 뒤에 있는 숫자를 2진수로 변환
# "{:b}".format(10)

# 뒤에 있는 숫자를 10진수로 변환
# int("1010", 2)


# 반복 가능한 객체(문자열, 리스트, 범위 등)에는 count() 함수를 사용할 수 있다.

# 위 두가지를 기반으로 1~100 사이에 있는 숫자 중 2진수로 변환했을 때 0이 하나만 포함된 숫자를 찾고, 
# 그 숫자들의 합을 구하는 코드를 만들어 보자.
# 1~100 / 2진수 / 0이 하나만 포함된 숫자 > 합 !!


output = 0      # output을 0으로 두고 이 내부로 들어왔을 때 i를 더해주게 끔 코드 작성
for i in range(1, 100 + 1):
    if "{:b}".format(i).count("0") == 1:
        print("{} : {:b}".format(i, i))     # "{:b}".format(i)
        output += i     # output = output + i 와 동일한 식이니까 i의 출력 값이 나올때마다 output에 쌓여 더해진다.
print("합계: {}".format(output))



# 리스트 내포 사용하는 방법 ver

output_2 = [u for u in range(1, 100 + 1)  if "{:b}".format(u).count("0") == 1]      # 변수 선언, for과 if를 한 줄로 + 결과 값 중에 i를 뽑아서 리스트를 만들어 줌
for u in output_2:
    print("{} : {}".format(u, "{:b}".format(u)))
print("합계: {}".format(sum(output_2)))


# 리스트 내포 사용하는 방법 ver2
output_3 = [z for z in range(1, 100 + 1)  if "{:b}".format(z).count("0") == 1]      # 변수 선언, for과 if를 한 줄로 + 결과 값 중에 i를 뽑아서 리스트를 만들어 줌
print(output_3)
print("합계: {}".format(sum(output_3)))