import pandas as pd
import numpy as np

# 간단한 집계를 넘어서서 조건부로 집계하고 싶은 경우
df = pd.DataFrame(
    {
        "key": ["A", "B", "C", "A", "B", "C"],
        "data1": [1, 2, 3, 1, 2, 3],
        "data2": np.random.randint(0, 6, 6),
    }
)

print(df, "\n")
print(df.groupby("key"), "\n")  # 한개로 그룹 묶기
print(df.groupby("key").sum(), "\n")  # 한개로 그룹 묶어서 합산 구하기
print(df.groupby(["key", "data1"]).sum(), "\n")  # 여러개로 그룹 묶어서 합산 구하기

# groupby를 통해서 집계를 한번에 계산하는 방법
print(df.groupby("key").aggregate(["min", np.median, max]), "\n")
print(df.groupby("key").aggregate({"data1": "min", "data2": np.sum}), "\n")

# groupby를 통해서 그룹 속성을 기준으로 데이터 필터링
def filter_by_mean(x):
    return x["data2"].mean() > 3


print(df.groupby("key").mean(), "\n")
print(df.groupby("key").filter(filter_by_mean), "\n")

# groupby를 통해서 묶인 데이터에 함수 적용
print(df.groupby("key").apply(lambda x: x.max() - x.min()))

# groupby로 묶인 데이터에서 key값으로 데이터를 가져올 수 있다.
# df = pd.read_csv("./univ.csv")
# print(df.head(), "\n")
# print(df.groupby("시도").get_group("충남"))
# print(len(df.gropby("시도").get_group("충남")))
