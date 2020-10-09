import matplotlib.pyplot as plt

# from elice_utils import EliceUtils
import preprocess

# elice_utils = EliceUtils()
team_goal_2014 = preprocess.team_goal_2014
"""
출력 형식을 위한 스켈레톤 코드입니다.
아래 줄 부터 문제에 맞는 코드를 작성해주세요.
"""
team_goal_2014.plot(
    x=team_goal_2014.index,
    y=team_goal_2014.values,
    kind="bar",
    figsize=(12, 12),
    fontsize=14,
)

# fig, ax = plt.subplots()
# ax.bar(team_goal_2014.index, team_goal_2014.values)
# plt.xticks(rotation = 90)
# plt.tight_layout()

plt.savefig(
    "D:\\Code\\Study\\NIPA_Study_Code\\월드컵 데이터 분석해보기\\result\\image.svg", format="svg"
)
# elice_utils.send_image("image.svg")
