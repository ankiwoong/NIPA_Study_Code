import pandas as pd
import numpy as np


def main():
    # 파일을 읽어서 코드를 작성해보세요
    # 경로: "./data/the_pied_piper_of_hamelin.csv"
    df = pd.read_csv(
        "D:\\Code\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 심화 알아보기\\data\\the_pied_piper_of_hamelin.csv"
    )
    print(df, "\n")

    # 아이들만 추출
    children = df[df["구분"] == "Child"]
    print(children, "\n")

    # 일차 별 평균 나이
    print(children.groupby("일차").mean(), "\n")

    # 일차 별 남자 / 여자 평균 나이
    df2 = children.pivot_table(index="일차", columns="성별", values="나이", aggfunc=np.mean)
    print(df2, "\n")

    # 피리 부는 사나이를 한번이라도 따라간 아이들
    for name in children["이름"].unique():
        print(name)


if __name__ == "__main__":
    main()