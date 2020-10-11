# from elice_utils import EliceUtils

# elice_utils = EliceUtils()
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

fname = (
    "D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\font\\NanumBarunGothic.ttf"
)
font = fm.FontProperties(fname=fname).get_name()
plt.rcParams["font.family"] = font


x = np.array(["축구", "야구", "농구", "배드민턴", "탁구"])
y = np.array([18, 7, 12, 10, 8])

z = np.random.randn(1000)


fig, axes = plt.subplots(1, 2, figsize=(8, 4))

# Bar 그래프
axes[0].bar(x, y)
# 히스토그램
axes[1].hist(z, bins=50)


# elice에서 그래프 확인하기
fig.savefig("D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\result\\plot.png")
# elice_utils.send_image("plot.png")
