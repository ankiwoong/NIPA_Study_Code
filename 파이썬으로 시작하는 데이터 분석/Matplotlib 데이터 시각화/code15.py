import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Histogram
fig, ax = plt.subplots()

data = np.random.randn(1000)
ax.hist(data, bins=50)

plt.show()