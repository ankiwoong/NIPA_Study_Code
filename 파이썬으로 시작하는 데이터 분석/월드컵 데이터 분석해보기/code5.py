import pandas as pd
import numpy as np

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

# 데이터 전처리를 위해 데이터 프레임의 일부 값을 replace 함수를 사용해 교체해줍니다.
world_cups_matches = world_cups.replace("Germany FR", "Germany")
print(world_cups_matches, "\n")

# 데이터 프레임에 중복된 데이터가 얼마나 있는지 확인할 수 있습니다.
dupli = world_cups_matches.duplicated()
print(len(dupli[dupli == True]), "\n")

# 중복값을 제거해야 합니다.
world_cups_matches = world_cups_matches.drop_duplicates()
print(world_cups_matches)