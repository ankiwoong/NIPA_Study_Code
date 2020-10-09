import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
world_cups = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\월드컵 데이터 분석해보기\\data\\WorldCups.csv"
)
"""
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
"""
world_cups = world_cups[["Year", "GoalsScored", "MatchesPlayed"]]
world_cups["GoalsPerMatch"] = world_cups["GoalsScored"] / world_cups["MatchesPlayed"]


# 첫 번째 그래프 출력
fig, axes = plt.subplots(2, 1, figsize=(4, 8))

axes[0].bar(
    x=world_cups["Year"], height=world_cups["GoalsScored"], color="grey", label="goals"
)

axes[0].plot(
    world_cups["Year"],
    world_cups["MatchesPlayed"],
    marker="o",
    color="blue",
    label="matches",
)

axes[0].legend(loc="upper left")


# 두 번째 그래프 출력
axes[1].grid(True)
axes[1].plot(
    world_cups["Year"],
    world_cups["GoalsPerMatch"],
    marker="o",
    color="red",
    label="goals_per_matches",
)

axes[1].legend(loc="lower left")

plt.savefig(
    "D:\\Code\\Study\\NIPA_Study_Code\\월드컵 데이터 분석해보기\\result\\image.svg", format="svg"
)
# elice_utils.send_image("image.svg")