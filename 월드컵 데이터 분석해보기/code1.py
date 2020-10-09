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

world_cups = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\월드컵 데이터 분석해보기\\data\\WorldCups.csv"
)
print(world_cups, "\n")

world_cups = world_cups[["Year", "Attendance"]]
print(world_cups, "\n")
