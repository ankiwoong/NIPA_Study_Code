# from elice_utils import EliceUtils
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# elice_utils = EliceUtils()

fig, ax = plt.subplots()
x = np.arange(10)
ax.plot(x, x ** 2, "o", markersize=15, markerfacecolor="white", markeredgecolor="blue")

fig.savefig("D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\result\\plot.png")
# elice_utils.send_image("plot.png")
