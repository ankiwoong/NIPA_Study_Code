import numpy as np

# 배열의 기초
x2 = np.random.randint(10, size=(3, 4))

print(x2)
print(x2.ndim)  # 차원
print(x2.shape)  # 행렬과 배열의 모양
print(x2.size)  # 원소의 크기
print(x2.dtype)  # 데이터 타입

print("-" * 20)

# 찾고 잘라내기
# indexing : 인덱스로 값을 찾아낸다.
x = np.arange(7)

print(x)
print(x[3])
# print(x[7])           # 범위 밖이므로 인덱스에러
x[0] = 10
print(x[0])

print("-" * 20)

# slicing : 인덱스 값으로 배열의 부분을 가져오는 것.
print(x)
print(x[1:4])
print(x[1:])
print(x[:4])
print(x[::2])