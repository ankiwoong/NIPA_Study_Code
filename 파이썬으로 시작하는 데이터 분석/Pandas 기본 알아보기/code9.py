import pandas as pd
import numpy as np

# 값으로 정렬하기
# sort_values()

df = pd.DataFrame(
    {
        "col1": [2, 1, 9, 8, 7, 4],
        "col2": ["A", "A", "B", np.nan, "D", "C"],
        "col3": [0, 1, 9, 4, 2, 3],
    }
)

print(df, "\n")
print(df.sort_values("col1"), "\n")  # 오름차순 정렬(기본)
print(df.sort_values("col1", ascending=False), "\n")  # 내림차순 정렬
print(df.sort_values(["col1", "col2"]))
