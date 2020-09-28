import numpy as np
import pandas as pd

# 조건으로 검색하기
# Numpy array와 마찬가지로 masking 연산이 가능하다.
df = pd.DataFrame(np.random.rand(5, 2), columns=["A", "B"])

print(df, "\n")
print(df["A"] < 0.5, "\n")  # 한기지 조건

# 조건에 맞는 DataFrame row를 추출 가능하다.
print(df[(df["A"] < 0.5) & (df["B"] > 0.3)], "\n")  # 두가지 조건
print(df.query("A < 0.5 and B > 0.3"))

# 문자열이라면 다른 방식으로도 조건 검색이 가능하다.
df = pd.read_csv(
    "D:\\Code\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 심화 알아보기\\data\\sample.csv"
)
print(df, "\n")
print(df["Animal"].str.contains("Cat"), "\n")
print(df.Animal.str.match("Cat"), "\n")
print(df["Animal"] == "Cat", "\n")
