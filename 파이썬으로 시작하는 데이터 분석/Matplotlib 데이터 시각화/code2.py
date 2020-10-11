# from elice_utils import EliceUtils
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# elice_utils = EliceUtils()

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]
# 그래프를 그리는 코드 작성
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("First Plot")
ax.set_xlabel("x")
ax.set_ylabel("y")


# elice에서 그래프를 확인
fig.savefig(
    "D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\result\\first_plot.png"
)
# elice_utils.send_image("first_plot.png")