import numpy as np
from numpy.lib.function_base import sinc

# 루프는 느리다
# array의 모든 원소에 5를 더해서 만드는 함수
def add_five_to_array(values):
    output = np.empty(len(values))

    for i in range(len(values)):
        output[i] = values[i] + 5

    return output


values = np.random.randint(1, 10, size=5)

print(add_five_to_array(values))

print("-" * 20)

# 만약 array의 크기가 크다면...?
big_array = np.random.randint(1, 100, size=10000000)

print(add_five_to_array(big_array))

print(big_array + 5)

print("-" * 20)

# 기본 연산
# array는 +, -, *, / 에 대한 기본 연산을 지원한다.
x = np.arange(4)

print(x)
print(x + 5)
print(x - 5)
print(x * 5)
print(x / 5)

print("-" * 20)

# 행렬간 연산
# 다차원 연산에서도 적용이 가능하다.
x = np.arange(4).reshape((2, 2))
y = np.random.randint(10, size=(2, 2))

print(x)
print(y)

print(x + y)  # 2 x 2 행렬
print(x - y)  # 2 x 2 행렬
