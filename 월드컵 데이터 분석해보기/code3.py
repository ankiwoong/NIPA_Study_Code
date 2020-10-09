import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
"""
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
"""
# WorldCups.csv파일을 pandas의 DataFrame으로 만들어보세요.
world_cups = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\월드컵 데이터 분석해보기\\data\\WorldCups.csv"
)
print(world_cups, "\n")

# 만든 데이터 프레임의 칼럼 중 Year 와 GoalsScored, MatchesPlayed 칼럼만 추출해보세요.
world_cups = world_cups[["Year", "GoalsScored", "MatchesPlayed"]]
print(world_cups, "\n")

# 데이터 프레임에 경기당 득점 수를 의미하는 새로운 칼럼 GoalsPerMatch를 추가합니다.
# GoalsPerMatch 의 값은 GoalsScored / MatchesPlayed입니다.
goalspermatch = world_cups["GoalsScored"] / world_cups["MatchesPlayed"]
world_cups["GoalsPerMatch"] = goalspermatch
print(world_cups)