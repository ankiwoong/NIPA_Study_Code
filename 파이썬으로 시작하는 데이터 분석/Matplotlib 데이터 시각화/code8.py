import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 범례
x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()

ax.plot(x, x, label="y=x")
ax.plot(x, x ** 2, label="y=x^2")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(
    loc="upper right",  # 범례 위치
    shadow=True,  # 그림자
    fancybox=True,  # 모서리 둥글게
    borderpad=2,  # 범례 데이터 크기
)

plt.show()