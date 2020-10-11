# from elice_utils import EliceUtils
import pandas as pd
import numpy as np

# elice_utils = EliceUtils()


def main():
    # 파일을 읽어서 코드를 작성해보세요
    # # 경로: "./data/the_pied_piper_of_hamelin.csv"
    df = pd.read_csv(
        "D:\\Code\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\실력 확인 테스트\\data\\the_pied_piper_of_hamelin.csv"
    )
    # print(df)
    df = df[df["구분"] == "Rat"]
    # print(df)
    rat = df.pivot_table(index="일차", columns="성별", values="나이", aggfunc=np.mean)
    print(rat)


if __name__ == "__main__":
    main()