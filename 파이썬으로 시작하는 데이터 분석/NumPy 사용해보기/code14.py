import numpy as np

# 집계 함수
# 집계 : 데이터에 대한 요약 통계를 볼 수 있다.
x = np.arange(8).reshape((2, 4))

print(x)
print(np.sum(x))  # 전체 합
print(np.min(x))  # 가장 작은 값
print(np.max(x))  # 가장 큰 값
print(np.mean(x))  # 평균
print(np.std(x))  # 표준 편차

print("-" * 20)

print(np.sum(x, axis=0))  # 세로 방향
print(np.sum(x, axis=1))  # 가로 방향

# 마스킹 연산 : Treu, False array를 통해서 특정 값들을 뽑아내는 방법
x = np.arange(5)

print(x < 3)  # x가 3보다 작은 숫자는 True / 큰 숫자는 False
print(x > 5)  # x가 5보다 큰 숫자는 True / 작은 숫자는 False
print(x[x < 3])  # array를 인덱스에 넣을 경우 조건에 True 인 값만 들어간다.
