import pandas as pd
import numpy as np

population_dict = {
    "korea": 5180,
    "japan": 12718,
    "china": 141500,
    "usa": 32676,
}
polulation = pd.Series(population_dict)

gdp_dict = {
    "korea": 169320000,
    "japan": 517670000,
    "china": 1409250000,
    "usa": 2041280000,
}
gdp = pd.Series(gdp_dict)

country = pd.DataFrame({"population": polulation, "gdp": gdp})

gdp_per_capita = country["gdp"] / country["population"]
country["gdp per capita"] = gdp_per_capita

# Indexing / Slicing
# loc : 명시적인 인덱스를 참조하는 인덱싱/슬라이싱
print(country)
print()

print(country.loc["china"])
print()

print(country.loc["japan":"korea", :"population"])
print()

# iloc : 파이썬 스타일 정수 인덱스 인덱싱/슬라이싱
print(country.iloc[0])
print()

print(country.iloc[1:3, :2])
print()

# DataFrame새 데이터 추가/수정
# 리스트로 추가하는 방법과 딕셔너리로 추가하는 방법
dataframe = pd.DataFrame(columns=["이름", "나이", "주소"])
dataframe.loc[0] = ["임원균", "26", "서울"]
dataframe.loc[1] = {"이름": "철수", "나이": "25", "주소": "인천"}

dataframe.loc[1, "이름"] = "영희"

print(dataframe)
print()

# 새로운 컬럼추가
dataframe["전화번호"] = np.nan
dataframe.loc[0, "전화번호"] = "01012341234"

print(len(dataframe))

# 컬럼이름이 하나만 있다면 Series
# 리스트로 들어가 잇다면 DataFrame
print(dataframe["이름"])
print()
print(dataframe[["이름", "주소", "나이"]])
