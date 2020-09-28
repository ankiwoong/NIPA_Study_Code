# from elice_utils import EliceUtils
import pandas as pd

# elice_utils = EliceUtils()


def main():
    # ./data/tree_data.csv 파일을 읽어서 작업해보세요!
    tree_df = pd.read_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 기본 알아보기\\data\\tree_data.csv"
    )
    tree_df = tree_df.sort_values("height", ascending=False)
    # print(tree_df.iloc[:5])     # 암묵적 인덱싱
    print(tree_df.head(5))
    tree_df.to_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 기본 알아보기\\result\\tree_data_sort.csv"
    )


if __name__ == "__main__":
    main()