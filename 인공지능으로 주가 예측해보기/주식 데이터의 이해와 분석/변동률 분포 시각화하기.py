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
    print(df)

    """
    주식 데이터 전처리하기
    """
    # 당일 종가가 아니라 다음 날 종가를 새로운 컬럼으로 추가해보기
    df["tomorrow Adj Close"] = df["Adj Close"].shift(-1)

    # 주가 변동 및 변동율(%) 추가하기 - 기대 수익률 계산 가능
    df["Fluctuation"] = df["tomorrow Adj Close"] - df["Adj Close"]
    df["Fluctuation Rate"] = df["Fluctuation"] / df["Adj Close"]

    # 히스토그램을 이용해 분포 살펴보기
    df["Fluctuation Rate"].plot.hist()
    plt.title("Fluctuation Rate Histogram")

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig("D:\\Code\\Study\\NIPA_Study_Code\\주식 데이터의 이해와 분석\\result\\plot-1.png")
    # elice_utils.send_image("plot.png")
    plt.cla()  # 그래프를 그린 후 초기화

    # 커널 밀도함수를 이용해 분포 살펴보기
    df["Fluctuation Rate"].plot.kde()
    plt.title("Fluctuation Rate Histogram")

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig("D:\\Code\\Study\\NIPA_Study_Code\\주식 데이터의 이해와 분석\\result\\plot-2.png")
    # elice_utils.send_image("plot.png")


if __name__ == "__main__":
    main()