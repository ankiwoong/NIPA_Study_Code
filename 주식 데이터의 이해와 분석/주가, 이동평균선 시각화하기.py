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
    ma5 = df["Adj Close"].rolling(window=5).mean()
    ma20 = df["Adj Close"].rolling(window=20).mean()
    ma60 = df["Adj Close"].rolling(window=60).mean()

    df.insert(len(df.columns), "MA5", ma5)
    df.insert(len(df.columns), "MA20", ma20)
    df.insert(len(df.columns), "MA60", ma60)

    vma5 = df["Volume"].rolling(window=5).mean()
    df.insert(len(df.columns), "VMA5", vma5)

    """
    이동평균선, 주가의 시각화
    """

    # 차트에 표현할 요소 설정
    plt.plot(df["Adj Close"], label="Adj Close")
    plt.plot(df["MA5"], label="MA5")
    plt.plot(df["MA20"], label="MA20")
    plt.plot(df["MA60"], label="MA60")

    #'best'를 인자로 주어 가장 적절한 자리에 위치하게 함
    plt.legend(loc="best")

    # 격자 그리기
    plt.grid()

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig("D:\\Code\\Study\\NIPA_Study_Code\\주식 데이터의 이해와 분석\\result\\plot.png")
    # elice_utils.send_image("plot.png")


if __name__ == "__main__":
    main()