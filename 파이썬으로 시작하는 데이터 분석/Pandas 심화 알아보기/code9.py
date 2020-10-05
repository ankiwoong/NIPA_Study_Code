import pandas as pd
import numpy as np

# MultiIndex
# 인덱스를 계층적으로 만들 수 있다.
df = pd.DataFrame(
    np.random.randn(4, 2),
    index=[["A", "A", "B", "B"], [1, 2, 1, 2]],
    columns=["data1", "data2"],
)

print(df, "\n")

# 열 인덱스도 계층적으로 만들 수 있다.
df = pd.DataFrame(
    np.random.randn(4, 4), columns=[["A", "A", "B", "B"], ["1", "2", "1", "2"]]
)

print(df, "\n")

# 다중 인덱스 컬럼의 경우 인덱싱은 계층적으로 한다.
# 인덱스 탐색의 경우에는 loc, iloc를 사용가능하다.
print(df["A"], "\n")
print(df["A"]["1"])

# Pivot_table
# 데이터에서 필요한 자료만 뽑아서 새롭게 요약,
# 분석 할 수 있는 기능 엑셀에서의 피봇 테이블과 같다
# index는 행 인덱스로 들어갈 key
# column에 열 인덱스로 라벨링 될 값
# value에 분석할 데이터
df = pd.read_csv(
    "D:\\Code\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 심화 알아보기\\data\\sample3.csv"
)

print(df, "\n")

# 타이타닉 데이터에서 성별과 좌석별 생존률 구하기
print(df.pivot_table(index="sex", columns="pclass", values="survived", aggfunc=np.mean))

# df.piviot_table(index="월별", columns="내역", values=["수입", "지출"])
