# from elice_utils import EliceUtils
import pandas as pd

# elice_utils = EliceUtils()


def main():
    # ./data/tree_data.csv 파일을 읽어서 작업해보세요!
    df = pd.read_csv(
        "D:\\Code\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\실력 확인 테스트\\data\\tree_data.csv"
    )
    # print(df) df = df.sort_values("circumference", ascending = False)
    # print(df)
    print(df.iloc[0])


if __name__ == "__main__":
    main()
