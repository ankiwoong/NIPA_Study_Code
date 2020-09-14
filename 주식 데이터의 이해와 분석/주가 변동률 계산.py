from datetime import datetime  # 날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt

# from elice_utils import EliceUtils

# elice_utils = EliceUtils()


def main():
    """
    주식 데이터 불러오기
    """
    df = pd.read_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\주식 데이터의 이해와 분석\\data\\stock.csv"
    )

    # 데이터 프레임 기본 형 출력
    # row X columns로 이루어진 table 모양
    """
    주가 변동 및 변동률 추가하기
    """
    # 당일 종가가 아니라 다음 날 종가를 새로운 컬럼으로 추가해보기
    df["tomorrow Adj Close"] = df["Adj Close"].shift(-1)

    # 주가 변동 및 변동률(%) 추가하기 - 기대 수익률 계산 가능
    df["Fluctuation"] = df["tomorrow Adj Close"] - df["Adj Close"]
    df["Fluctuation Rate"] = df["Fluctuation"] / df["Adj Close"]

    print(df)


if __name__ == "__main__":
    main()