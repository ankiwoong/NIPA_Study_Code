import numpy as np
from numpy.core.defchararray import lower

# 모양 바꾸기
# reshape : array의 shape를 변경한다.
x = np.arange(8)

print(x)
print(x.shape)

x2 = x.reshape((2, 4))

print(x2)
print(x2.shape)

print("-" * 20)

# 이어 붙이고 나누기
# concatenate : array를 이어 붙인다.
x = np.array([0, 1, 2])
y = np.array([3, 4, 5])

print(x)
print(y)
print(np.concatenate([x, y]))

print("-" * 20)

# np.concatenate : asix 축을 기준으로 이어붙일 수 있다.
matrix = np.arange(4).reshape(2, 2)

print(matrix)  # 기본 / 2 x 2
print(np.concatenate([matrix, matrix], axis=0))  # 세로방향으로 이어붙임 / 4 x 2
print(np.concatenate([matrix, matrix], axis=1))  # 가로방향으로 이어붙임 / 2 x 4

print("-" * 20)

# np.split : asix 축을 기준으로 나눌 수 있다.
matrix = np.arange(16).reshape(4, 4)

upper_, lower_ = np.split(matrix, [3], axis=0)  # 인덱스 3번을 기준으로 세로방향으로 나눔
left_, right_ = np.split(matrix, [3], axis=1)  # 인덱스 3번을 기준으로 가로방향으로 나눔

print(matrix)  # 기본 / 4 x 4
print(upper_, lower_)
print(left_, right_)