import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
import preprocess

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
"""
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
"""
# 이전에 전처리한 WorldCupMatches.csv파일이 주어집니다.
world_cups_matches = preprocess.world_cups_matches

# 전처리를 거친 데이터 프레임에서 홈 팀 득점을 나타내는 home 데이터 프레임과, away 팀 득점을 나타내는 away 데이터 프레임을 각각 만들어보고자 합니다.
# Home Team Name으로 그룹을 묶고, Home Team Goals 칼럼을 추출하여 home에 저장합니다.
# Away Team Name으로 그룹을 묶고, Away Team Goals 칼럼을 추출하여 away에 저장합니다.
home = world_cups_matches.groupby(["Home Team Name"])["Home Team Goals"].sum()
away = world_cups_matches.groupby(["Away Team Name"])["Away Team Goals"].sum()

# goal_per_country 데이터 프레임에 새로운 칼럼 “Goals”를 만들도록 하겠습니다.
# Home Team Goals와 Away Team Goals 를 덧셈 연산한 값을 Goals에 저장합니다.
goal_per_country = pd.concat([home, away], axis=1, sort=True).fillna(0)
print(goal_per_country)

# goal_per_country 에서 Goals 칼럼만 추출하고, 내림차순으로 정렬합니다.
# (이 때, goal_per_country는 시리즈 데이터가 됩니다.)
goal_per_country["Goals"] = (
    goal_per_country["Home Team Goals"] + goal_per_country["Away Team Goals"]
)
goal_per_country = goal_per_country["Goals"].sort_values(ascending=False)
print(goal_per_country)

# 저장된 값의 dtype를 정수형으로 바꿉니다.
goal_per_country = goal_per_country.astype(int)
print(goal_per_country)