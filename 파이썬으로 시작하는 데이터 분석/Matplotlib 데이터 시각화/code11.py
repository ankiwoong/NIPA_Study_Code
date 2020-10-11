import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Scatter

fig, ax = plt.subplots()

x = np.random.randn(50)
y = np.random.randn(50)

colors = np.random.randint(0, 100, 50)
sizes = 500 * np.pi * np.random.rand(50) ** 2
ax.scatter(
    x,
    y,
    c=colors,
    s=sizes,
    alpha=0.3,
)

plt.show()