import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Color
x = np.arange(10)

fig, ax = plt.subplots()

ax.plot(x, x, color="r")  # 색상 축약어(r, g, b, c, h, y, k)
ax.plot(x, x + 2, color="green")  # 색상 풀네임
ax.plot(x, x + 4, color="0.8")  # 0 ~ 1 회색
ax.plot(x, x + 6, color="#524FA1")  # 16진수 색상 코드

plt.show()