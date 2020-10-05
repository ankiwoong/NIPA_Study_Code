import matplotlib.pyplot as plt
import numpy as np

# 그래프 그려보기 1
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

plt.plot(x, y)
plt.title("First Plot")
plt.xlabel("x")
plt.ylabel("y")

# plt.show()

# 그래프 그려보기 2
x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("First Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")

# 그래프 저장하기
fig.set_dpi(300)  # 해상도
fig.savefig(
    "D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\result\\first_plot.png"
)  # 저장 위치

# 여러개 그래프 그리기
x = np.linspace(0, np.pi * 4, 100)
fig, axes = plt.subplots(2, 1)
axes[0].plot(x, np.sin(x))
axes[1].plot(x, np.cos(x))

plt.show()