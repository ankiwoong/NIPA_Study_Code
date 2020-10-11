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
# WorldCups.csv 을 데이터 프레임으로 만든 변수 world_cups가 주어졌습니다.
world_cups = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\월드컵 데이터 분석해보기\\data\\WorldCups.csv"
)

# 데이터 프레임에서 역대 대회 1위 국가, 2위 국가, 3위 국가, 4위 국가를 추출하여 각각 변수 winner, runners_up, third, fourth에 저장하도록 하겠습니다.
winner = world_cups["Winner"]
runners_up = world_cups["Runners-Up"]
third = world_cups["Third"]
fourth = world_cups["Fourth"]

# value_counts 함수를 이용해 각 시리즈 데이터에 저장된 값을 세어주고 저장합니다.
# 이 작업을 거치면, 국가별 1위, 2위, 3위, 4위 횟수가 각각 저장된 데이터가 만들어집니다.
winner_count = pd.Series(winner.value_counts())
print(winner_count, "\n")

runners_up_count = pd.Series(runners_up.value_counts())
third_count = pd.Series(third.value_counts())
fourth_count = pd.Series(fourth.value_counts())

# 위 데이터들을 하나의 데이터 프레임으로 합치도록 하겠습니다.
ranks = pd.DataFrame(
    {
        "Winner": winner_count,
        "Runners_up": runners_up_count,
        "Third": third_count,
        "Fourth": fourth_count,
    }
)

# ranks에 들어있는 값이 NaN이라면, 해당 순위를 기록한 적이 없다는 의미입니다.
# 따라서 데이터의 결측값을 0으로 채우고, dtype을 int64로 다시 설정합니다
ranks = ranks.fillna(0).astype("int64")

# 각 국가들을 우승 횟수, 준우승 횟수, 3위 횟수, 4위 횟수 순서대로 내림차순 정렬하세요.
ranks = ranks.sort_values(["Winner", "Runners_up", "Third", "Fourth"], ascending=False)
print(ranks)