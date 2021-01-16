# 혼자 공부하는 파이썬 35강 - 재귀함수와 메모화 (함수를 사용하는 일종의 테크닉)

# 팩토리얼 구현하기
# n! = 1 * 2 * 3 * ... (n-2) * (n-1) * n
def factorial_1(n):
    변수 = 1
    for i in range(1, n + 1):
        변수 *= i
    return 변수

# n! = n * (n-1)!
# 0! = 1

def factorial_2(n):
    if n == 0:
        return 1
    else:
        return n * factorial_2(n-1)         # 함수 내부에서 함수를 호출하는 함수 = 재귀 함수

print(factorial_1(10))
print(factorial_2(10))


# 재귀 함수의 문제
# feat. 피버나츠 수열 (토끼가 어떤 속도로 번식하는가)

# f(1) = 1
# f(2) = 1
# f(n) = f(n-1) + f(n-2)

# 이를 통해 나뭇가지의 갯수, 꽃잎의 갯수 등을 구할 수 있음.

def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)

print(f(1))
print(f(2))
print(f(3))
print(f(4))

# 이러한 식으로 피버나츠 수열을 구하게 되면 약간의 문제가 발생한다.
# 수열을 40 정도를 구하게 되면 값을 계산하는데 매우 오랜 시간이 걸림.

# 대체 계산이 몇번이 이루어지고 있길래 이러한 문제가 발생하는지 counter 함수로 확인해보자.


counter = 0
def f(n):
    global counter          # 함수 내부에서 외부에 있는 변수에 접근할 때는 global 이라는 키워드를 사용을 해서 정의를 해줘야 한다.
    counter += 1
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1) + f(n-2)
print(f(10))
print(counter)
print(f(20))
print(counter)
print(f(30))
print(counter)

# 계산이 오래 걸리는 이유는 구했던 것을 여러번 반복해서 구하기 때문에 발생하는 문제이다.
# 이 문제를 해결할 때 사용하는 것이 '메모화(memoization)' 라는 기술이다.

메모 = { 1: 1, 2: 1 }       # 레퍼런스를 나타내는 자료형 같은 경우에는 global을 사용하지 않아도 된다.
def f(n):
    if n in 메모:
        return 메모[n]
    else:
        output = f(n-1) + f(n-2)
        메모[n] = output
        return output

print(f(40))

# 재귀함수를 사용할 때 재귀함수를 계산하는데 시간이 너무 오래 걸린다면 이 메모화를 꼭 함께 사용해야 한다.



# 조기 리턴
# 과거에 프로그래밍을 할 때는 어떤 함수의 시작 부분에 변수 선언을 하고, 최종적인 블럭에 마지막 단계에서 return을 해주라고 되어 있었다.
# 현대에는 그냥 한 블럭 내부에서 return이 2번 나오는 코드로 작성하는 것이 더 깔끔하다고 생각.
# else를 쓰지 않고 return만 2번 (들여쓰기 단계를 줄이는 것임.)

