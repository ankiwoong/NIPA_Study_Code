import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 축 경계 조정하기
x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x))
ax.set_xlim(-2, 12)  # x축의 시작, 끝
ax.set_ylim(-1.5, 1.5)  # y축의 시작, 끝

plt.show()
