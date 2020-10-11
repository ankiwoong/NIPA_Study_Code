import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Marker
x = np.arange(10)

fig, ax = plt.subplots()

ax.plot(x, x, marker=".")
ax.plot(x, x + 2, marker="o")
ax.plot(x, x + 4, marker="v")
ax.plot(x, x + 6, marker="s")
ax.plot(x, x + 8, marker="*")

plt.show()