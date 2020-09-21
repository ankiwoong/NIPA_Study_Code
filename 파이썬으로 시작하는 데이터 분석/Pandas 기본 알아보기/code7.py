import pandas as pd
import numpy as np

dataframe = pd.DataFrame(columns=["이름", "나이", "주소"])
dataframe.loc[0] = ["임원균", "26", "서울"]
dataframe.loc[1] = {"이름": "철수", "나이": "25", "주소": "인천"}

dataframe.loc[1, "이름"] = "영희"

dataframe["전화번호"] = np.nan  # nan = not a number
dataframe.loc[0, "전화번호"] = "01012341234"

# 누락된 데이터 체크
# 튜토리얼에서 보는 데이터와 달리 현실의 데이터는 누락되어 있는 형태가 많다.
print(dataframe.isnull())
print()

print(dataframe.notnull())
print()

print(dataframe.dropna())
print()

dataframe["전화번호"] = dataframe["전화번호"].fillna("전화번호 없음")
print(dataframe)
print()

# numpy array에서 사용했던 연산자들을 활용할 수 있다.
A = pd.Series([2, 4, 6], index=[0, 1, 2])
B = pd.Series([1, 3, 5], index=[1, 2, 3])

print(A)
print()
print(B)
print()
print(A + B)
print()
print(A.add(B, fill_value=0))
print()

# add(+), sub(-), mul(*), div(/)
A = pd.DataFrame(np.random.randint(0, 10, (2, 2)), columns=list("AB"))
B = pd.DataFrame(np.random.randint(0, 10, (3, 3)), columns=list("BAC"))

print(A)
print()
print(B)
print()
print(A + B)
print()
print(A.add(B, fill_value=0))
print()

# numpy array에서 사용했던 sum, mean 등을 활용할 수 있다.
data = {"A": [i + 5 for i in range(3)], "B": [i ** 2 for i in range(3)]}

df = pd.DataFrame(data)
print(df["A"].sum())
print()
print(df.sum())
print()
print(df.mean())