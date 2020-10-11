import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Scatter

fig, ax = plt.subplots()

x = np.arange(10)

ax.plot(
    x,
    x ** 2,
    "o",  # 마커 모양
    markersize=15,  # 마커 사이즈
    markerfacecolor="white",  # 마커 안쪽 색상
    markeredgecolor="blue",  # 마커 외곽 색상
)

plt.show()