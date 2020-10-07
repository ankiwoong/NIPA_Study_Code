import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bar plot
x = np.arange(10)

fig, ax = plt.subplots(figsize=(12, 4))

ax.bar(x, x ** 2)

plt.show()