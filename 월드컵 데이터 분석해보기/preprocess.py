import pandas as pd
import numpy as np

world_cups = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\월드컵 데이터 분석해보기\\data\\WorldCups.csv"
)
winner = world_cups["Winner"]
runners_up = world_cups["Runners-Up"]
third = world_cups["Third"]
fourth = world_cups["Fourth"]
winner_count = pd.Series(winner.value_counts())
runners_up_count = pd.Series(runners_up.value_counts())
third_count = pd.Series(third.value_counts())
fourth_count = pd.Series(fourth.value_counts())
ranks = pd.DataFrame(
    {
        "Winner": winner_count,
        "Runners_Up": runners_up_count,
        "Third": third_count,
        "Fourth": fourth_count,
    }
)
ranks = ranks.fillna(0).astype("int")
ranks = ranks.sort_values(["Winner", "Runners_Up", "Third", "Fourth"], ascending=False)
