import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Matplotlib with pandas
df = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\data\\pokemon.csv"
)

print(df)

fire = df[(df["Type 1"] == "Fire") | ((df["Type 2"]) == "Fire")]
water = df[(df["Type 1"] == "Warter") | ((df["Type 2"]) == "Water")]

fig, ax = plt.subplots()

ax.scatter(fire["Attack"], fire["Defense"], color="r", label="Fire", marker="*", s=50)
ax.scatter(water["Attack"], water["Defense"], color="b", label="Water", s=25)
ax.set_xlabel("Attack")
ax.set_ylabel("Defense")
ax.legend(loc="upper right")

plt.show()