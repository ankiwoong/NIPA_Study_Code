from datetime import datetime  # 날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd


def main():
    """
    주식 데이터 불러오기
    """
    df = pd.read_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\주식 데이터의 이해와 분석\\data\\stock.csv"
    )

    # 데이터 프레임 기본 형 출력
    # row X columns로 이루어진 table 모양
    print(df)

    """
    주식 데이터 살펴보기
    """

    # 주식 데이터의 모양을 출력
    print(df.shape)

    # 주식 데이터의 정보를 출력
    print(df.info)

    # 주식 데이터의 타입(데이터 형태)을 출력
    print(df.dtypes)

    # 주식 데이터의 상단 5개의 값을 출력
    print(df.head())

    # 주식 테이터의 하단 5개의 값을 출력
    print(df.tail())

    # 주식 데이터의 columns를 모두 출력
    print(df.columns)

    # 주식 데이터의 요약 통계 자료 출력
    print(df.describe())


if __name__ == "__main__":
    main()