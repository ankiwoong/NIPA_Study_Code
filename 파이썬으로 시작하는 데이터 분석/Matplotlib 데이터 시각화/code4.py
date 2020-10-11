import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Line Style
x = np.arange(10)

flg, ax = plt.subplots()

ax.plot(x, x, linestyle="-")  # solid
ax.plot(x, x + 2, linestyle="--")  # dashed
ax.plot(x, x * 4, linestyle="-.")  # dashdot
ax.plot(x, x * 6, linestyle=":")  # dotted

plt.show()