import pandas as pd


def main():
    tree_df = pd.read_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 기본 알아보기\\data\\tree_data.csv"
    )
    # print(len(tree_df.dropna()))  # 누락된 데이터 확인
    tree_df = tree_df.sort_values("height", ascending=False)  # 내림차순 정렬
    # print(tree_df.iloc[:5])  # 암묵적 인덱스
    print(tree_df.head(5))  # 위에서 5개만 출력
    tree_df.to_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\파이썬으로 시작하는 데이터 분석\\Pandas 기본 알아보기\\result\\tree_data_sort.csv"
    )


if __name__ == "__main__":
    main()