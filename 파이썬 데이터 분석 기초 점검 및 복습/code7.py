import pandas as pd

# 코로나 데이터를 불러옵니다.
data_path = (
    "D:\\Code\\Study\\NIPA_Study_Code\\파이썬 데이터 분석 기초 점검 및 복습\\data\\corona_data.xlsx"
)
corona_data = pd.read_excel(data_path)

# .loc을 활용하여 7월 30일의 사망자 데이터를 추출해봅니다.
death_0730 = corona_data.loc[corona_data["날짜"] == "2020-07-30", "사망자"]
print(death_0730)