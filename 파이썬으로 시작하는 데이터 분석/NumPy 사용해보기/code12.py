import numpy as np

# 브로드캐스팅
# Broadcasting : shape이 다른 array끼리 연산
matrix_ = np.arange(9).reshape((3, 3))

print(matrix_)
print(matrix_ + 5)  # 다른 모양 연산
print(matrix_ + np.array([1, 2, 3]))

print(np.arange(3).reshape((3, 1)) + np.arange(3))
