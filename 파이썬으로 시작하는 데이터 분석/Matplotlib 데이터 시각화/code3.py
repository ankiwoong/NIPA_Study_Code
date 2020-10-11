import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Line plot
flg, ax = plt.subplots()

x = np.arange(15)
y = x ** 2
ax.plot(
    x,
    y,
    linestyle=":",
    marker="*",
    color="#524FA1",
)

plt.show()