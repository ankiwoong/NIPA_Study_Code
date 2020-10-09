import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
import preprocess

pd.set_option("display.max_rows", 500)
pd.set_option("display.max_columns", 500)
pd.set_option("display.width", 1000)
ranks = preprocess.ranks
"""
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
"""

# x축에 그려질 막대그래프들의 위치입니다.
x = np.array(list(range(0, len(ranks))))

# 그래프를 그립니다.
fig, ax = plt.subplots()

# x 위치에, 항목 이름으로 ranks.index(국가명)을 붙입니다.
plt.xticks(x, ranks.index, rotation=90)
plt.tight_layout()

# 4개의 막대를 차례대로 그립니다.
ax.bar(x - 0.3, ranks["Winner"], color="gold", width=0.2, label="Winner")
ax.bar(x - 0.1, ranks["Runners_Up"], color="silver", width=0.2, label="Runners_Up")
ax.bar(x + 0.1, ranks["Third"], color="brown", width=0.2, label="Third")
ax.bar(x + 0.3, ranks["Fourth"], color="black", width=0.2, label="Fourth")


plt.savefig(
    "D:\\Code\\Study\\NIPA_Study_Code\\월드컵 데이터 분석해보기\\result\\image.svg", format="svg"
)
# elice_utils.send_image("image.svg")