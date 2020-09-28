import numpy as np
import pandas as pd

print("DataFrame: ")
df = pd.DataFrame(
    {
        "col1": [2, 1, 9, 8, 7, 4],
        "col2": ["A", "A", "B", np.nan, "D", "C"],
        "col3": [0, 1, 9, 4, 2, 3],
    }
)
print(df, "\n")


# 정렬 코드 입력해보기
# Q1. col1을 기준으로 오름차순으로 정렬하기.
sorted_df1 = df.sort_values("col1", ascending=True)
print(sorted_df1, "\n")

# Q2. col2를 기준으로 내림차순으로 정렬하기.
sorted_df2 = df.sort_values("col2", ascending=False)
print(sorted_df2, "\n")

# Q3. col2를 기준으로 오름차순으로, col1를 기준으로 내림차순으로 정렬하기.
sorted_df3 = df.sort_values(["col2", "col1"], ascending=[True, False])
print(sorted_df3, "\n")
