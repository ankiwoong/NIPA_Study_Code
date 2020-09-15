# 배열 만들기
a = list(range(10))
print(a)

import numpy as np

b = np.array([1, 2, 3, 4, 5])
c = np.array([3, 1.4, 2, 3, 4])
d = np.array([[1, 2], [3, 4]])
e = np.array([1, 2, 3, 4], dtype="float")

print(b)
print(c)
print(d)
print(e)

print("-" * 20)

# 배열 데이터 타입 - dtype
"""
dtype
1. int - 정수형 타입
2. float - 실수형 타입
3. str - 문자열형 타입
4. bool - 부울 타입
"""
e = np.array([1, 2, 3, 4], dtype="float")  # dtype : 배열 데이터 타입

print(e.dtype)
print(e.astype(int))

print("-" * 20)

# 다양한 배열 만들기
f = np.zeros(10, dtype=int)  # 0을 10번 사용하여 정수형 배열 생성
g = np.ones((3, 5), dtype=float)  # 3 x 5 형태로 실수형 배열 생성
h = np.arange(0, 20, 2)  # 0 ~ 20 배열을 생성하는데 2씩 스탭을 주어서 배열 생성(range와 동일)
i = np.linspace(0, 1, 5)  # 0 ~ 1 까지 5개씩 균등하게 나눠서 배열 생성

print(f)
print(g)
print(h)
print(i)

print("-" * 20)

# 난수로 채워진 배열 만들기
j = np.random.random((2, 2))  # 2 x 2 형태로 임의의 숫자로 배열 생성
k = np.random.normal(0, 1, (2, 2))  # 평균이 0 이고 표준편차가 1인 데이터를 2 x 2 형태로 배열 생성
l = np.random.randint(0, 10, (2, 2))  # 0 부터 10까지 2 x 2 형태로 배열 생성

print(j)
print(k)
print(l)