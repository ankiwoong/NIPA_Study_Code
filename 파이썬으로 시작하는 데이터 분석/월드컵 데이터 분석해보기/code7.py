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

world_cups_matches = preprocess.world_cups_matches

world_cups_matches = world_cups_matches[world_cups_matches["Year"] == 2014]
# print(world_cups_matches)

home_team_goal = world_cups_matches.groupby(["Home Team Name"])["Home Team Goals"].sum()
away_team_goal = world_cups_matches.groupby(["Away Team Name"])["Away Team Goals"].sum()

team_goal_2014 = pd.concat([home_team_goal, away_team_goal], axis=1).fillna(0)

team_goal_2014["goals"] = (
    team_goal_2014["Home Team Goals"] + team_goal_2014["Away Team Goals"]
)
team_goal_2014 = team_goal_2014.drop(["Home Team Goals", "Away Team Goals"], axis=1)

team_goal_2014.astype("int")

team_goal_2014 = team_goal_2014["goals"].sort_values(ascending=False)
print(team_goal_2014)