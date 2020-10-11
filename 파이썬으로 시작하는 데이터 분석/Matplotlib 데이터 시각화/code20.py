# from elice_utils import EliceUtils
from matplotlib import pyplot as plt
import pandas as pd

plt.rcParams["font.family"] = "NanumBarunGothic"

# elice_utils = EliceUtils()


def main():
    # 아래 경로에서 csv파일을 읽어서 시각화 해보세요
    # 경로: "./data/the_hare_and_the_tortoise.csv"
    df = pd.read_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\data\\the_hare_and_the_tortoise.csv"
    )
    df.set_index("시간", inplace=True)
    print(df)

    fig, ax = plt.subplots()
    ax.plot(df["토끼"], label="토끼")
    ax.plot(df["거북이"], label="거북이")
    ax.legend()

    # 그래프를 확인하려면 아래 두 줄의 주석을 해제한 후 코드를 실행하세요.
    fig.savefig(
        "D:\\Code\\Study\\NIPA_Study_Code\\Matplotlib 데이터 시각화\\result\\plot.png"
    )
    # elice_utils.send_image("plot.png")


if __name__ == "__main__":
    main()
