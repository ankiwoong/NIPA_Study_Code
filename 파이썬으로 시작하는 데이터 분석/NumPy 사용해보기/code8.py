import numpy as np

print("matrix")
matrix = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
print(matrix)
print("shape : ", matrix.shape, "\n")

# (아래의 배열 모양을 참고하세요.)
# Q1. matrix 두 개를 세로로 붙이기
"""
[[0 1 2 3]
 [4 5 6 7]
 [0 1 2 3]
 [4 5 6 7]]
"""

m = np.concatenate([matrix, matrix], axis=0)
print(m)


# Q2. matrix 두 개를 가로로 붙이기
"""
[[0 1 2 3 0 1 2 3]
 [4 5 6 7 4 5 6 7]]
"""

n = np.concatenate([matrix, matrix], axis=1)
print(n)
