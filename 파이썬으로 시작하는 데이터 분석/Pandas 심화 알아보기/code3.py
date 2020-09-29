import pandas as pd
import numpy as np

# 함수로 데이터 처리하기
# apply를 통해서 함수로 데이터를 다룰 수 있다.
# Ex1>
df = pd.DataFrame(np.arange(5), columns=["Num"])


def square(x):
    return x ** 2


print(df["Num"].apply(square), "\n")

df["Square"] = df.Num.apply(lambda x: x ** 2)
print(df, "\n")

# Ex2>
df = pd.DataFrame(columns=["phone"])
df.loc[0] = "010-1234-1235"
df.loc[1] = "공일공-일이삼사-1235"
df.loc[2] = "010.1234.일이삼오"
df.loc[3] = "공1공-1234.1이3오"
df["preprocess_phone"] = ""

print(df, "\n")


def get_preprocess_phone(phone):
    mapping_dict = {
        "공": "0",
        "일": "1",
        "이": "2",
        "삼": "3",
        "사": "4",
        "오": "5",
        "-": "",
        ".": "",
    }
    for key, value in mapping_dict.items():
        phone = phone.replace(key, value)
    return phone


df["preprocess_phone"] = df["phone"].apply(get_preprocess_phone)

print(df, "\n")

# replace: apply 기능에서 데이터 값만 대체 하고 싶을때
df = pd.read_csv(
    "D:\\Code\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 심화 알아보기\\data\\sample2.csv"
)
print(df, "\n")
print(df.Sex.replace({"Male": 0, "Female": 1}), "\n")  # 변경 후 출력

df.Sex.replace({"Male": 0, "Female": 1}, inplace=True)  # 원본 수정 후 출력
print(df)