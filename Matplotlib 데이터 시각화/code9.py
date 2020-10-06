# from elice_utils import EliceUtils
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# elice_utils = EliceUtils()

# 이미 입력되어 있는 코드의 다양한 속성값들을 변경해 봅시다.
x = np.arange(10)
fig, ax = plt.subplots()
ax.plot(x, x, label="y=x", marker="o", color="blue", linestyle=":")
ax.plot(x, x ** 2, label="y=x^2", marker="^", color="red", linestyle="--")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend(loc="upper left", shadow=True, fancybox=True, borderpad=2)

fig.savefig("D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\result\\plot.png")
# elice_utils.send_image("plot.png")