# from elice_utils import EliceUtils
from matplotlib import pyplot as plt
import pandas as pd

# elice_utils = EliceUtils()
plt.rcParams["font.family"] = "NanumBarunGothic"


# 아래 경로에서 csv파일을 읽어서 시각화 해보세요
# 경로: "./data/WorldCups.csv"
df = pd.read_csv(
    "D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\data\\WorldCups.csv"
)  # 월드컵 정보를 담는 csv 파일을 읽어옵니다.
# 어떤 자료를 갖는지 직접 확인해보세요!
# print(df)
"""
    Year       Country      Winner      Runners-Up        Third          Fourth  GoalsScored  QualifiedTeams  MatchesPlayed Attendance
0   1930       Uruguay     Uruguay       Argentina          USA      Yugoslavia           70              13             18    590.549
1   1934         Italy       Italy  Czechoslovakia      Germany         Austria           70              16             17    363.000
2   1938        France       Italy         Hungary       Brazil          Sweden           84              15             18    375.700
3   1950        Brazil     Uruguay          Brazil       Sweden           Spain           88              13             22  1.045.246
4   1954   Switzerland  Germany FR         Hungary      Austria         Uruguay          140              16             26    768.607
5   1958        Sweden      Brazil          Sweden       France      Germany FR          126              16             35    819.810
6   1962         Chile      Brazil  Czechoslovakia        Chile      Yugoslavia           89              16             32    893.172
7   1966       England     England      Germany FR     Portugal    Soviet Union           89              16             32  1.563.135
8   1970        Mexico      Brazil           Italy   Germany FR         Uruguay           95              16             32  1.603.975
9   1974       Germany  Germany FR     Netherlands       Poland          Brazil           97              16             38  1.865.753
10  1978     Argentina   Argentina     Netherlands       Brazil           Italy          102              16             38  1.545.791
11  1982         Spain       Italy      Germany FR       Poland          France          146              24             52  2.109.723
12  1986        Mexico   Argentina      Germany FR       France         Belgium          132              24             52  2.394.031
13  1990         Italy  Germany FR       Argentina        Italy         England          115              24             52  2.516.215
14  1994           USA      Brazil           Italy       Sweden        Bulgaria          141              24             52  3.587.538
15  1998        France      France          Brazil      Croatia     Netherlands          171              32             64  2.785.100
16  2002   Korea/Japan      Brazil         Germany       Turkey  Korea Republic          161              32             64  2.705.197
17  2006       Germany       Italy          France      Germany        Portugal          147              32             64  3.359.439
18  2010  South Africa       Spain     Netherlands      Germany         Uruguay          145              32             64  3.178.856
19  2014        Brazil     Germany       Argentina  Netherlands          Brazil          171              32             64  3.386.810
"""

winners = df["Winner"]  # 읽어온 데이터 프레임 중 "우승국"을 의미하는 칼럼을 가져오세요.

# 국가 별 우승 횟수를 나타내는 딕셔너리 입니다.
winner_dict = {}


for i in winners:  # 우승국을 반복문으로 읽으며, 해당 국가의 우승 횟수를 1씩 증가시킵니다.
    if i in winner_dict:
        winner_dict[i] += 1
        # i(우승국)이 이미 winner_dict에 있다면, value를 1 증가시킵니다.
    else:
        winner_dict[i] = 1
        # i(우승국)이 winner_dict에 최초로 등장한다면, value를 1로 설정합니다.

print(winner_dict)

X = list(winner_dict.keys())  # X축 변수, 즉 우승국을 나타냅니다.
Y = list(winner_dict.values())  # Y축 변수, 즉 우승 횟수를 나타냅니다.

fig, ax = plt.subplots(figsize=(8, 8))

# ax.plot(X, Y)

ax.bar(X, Y)

ax.set_xlabel("Country")
ax.set_ylabel("Number")

ax.set_xticks(X)

fig.savefig("D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\result\\Winner.png")
# elice_utils.send_image("Winner.png")