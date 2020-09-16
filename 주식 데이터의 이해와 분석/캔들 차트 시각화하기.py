from datetime import datetime  # 날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import matplotlib.pyplot as plt

# matplotlib에서 x축과 y축에 표시되는 값을 ticker라 함
import matplotlib.ticker as ticker
import matplotlib.dates as mdates
import numpy as np

# from elice_utils import EliceUtils

# elice_utils = EliceUtils()


def main():
    """
    주식 데이터 불러오기
    """
    df = pd.read_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\주식 데이터의 이해와 분석\\data\\stock.csv",
        index_col=0,
        parse_dates=True,
    )

    # 데이터 프레임 기본 형 출력
    # row X columns로 이루어진 table 모양
    print(df)

    """
    캔들차트 시각화
    """

    # 차트와 피규어 그리기 준비 및 크기 설정
    mc = mpf.make_marketcolors(up="r", down="b")
    s = mpf.make_mpf_style(marketcolors=mc)
    mpf.plot(df, type="candle", figscale=1.2, style=s)

    plt.savefig("D:\\Code\\Study\\NIPA_Study_Code\\주식 데이터의 이해와 분석\\result\\plot.png")
    # elice_utils.send_image("plot.png")


if __name__ == "__main__":
    main()