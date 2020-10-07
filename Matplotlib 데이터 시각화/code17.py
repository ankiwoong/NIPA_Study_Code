import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Matplotlib with pandas
df = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\data\\president_heights.csv"
)
print(df)

fig, ax = plt.subplots()

ax.plot(df["order"], df["height(cm)"], label="height")
ax.set_xlabel("order")
ax.set_ylabel("height(cm)")
ax.legend()

plt.show()