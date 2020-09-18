import pandas as pd

# 코로나 데이터를 불러옵니다.
data_path = (
    "D:\\Code\\Study\\NIPA_Study_Code\\파이썬 데이터 분석 기초 점검 및 복습\\data\\corona_data.xlsx"
)
corona_data = pd.read_excel(data_path)

# 확진자가 10000명 이상인 시점부터의 모든 데이터를 추출합니다.
confirmed_10000 = corona_data.loc[corona_data["확진자"] >= 10000]
print(confirmed_10000)