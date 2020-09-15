from datetime import datetime  # 날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense, Activation

# from elice_utils import EliceUtils

# elice_utils = EliceUtils()


def main():
    """
    주식 데이터 불러오기
    """
    df = pd.read_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\주가 예측을 위한 인공지능 모델 만들기\\data\\stock.csv"
    )

    # 데이터 프레임 기본 형 출력
    # row X columns로 이루어진 table 모양
    print(df)

    """
    딥러닝의 입력피쳐 설계
    """
    # 가격의 중간값 계산하기
    high_prices = df["High"].values
    low_prices = df["Low"].values
    mid_prices = (high_prices + low_prices) / 2
    print(mid_prices)

    # 중간 값 요소 추가하기
    df["Mid"] = mid_prices
    print(df)

    # 이동평균값 계산하기
    ma5 = df["Adj Close"].rolling(window=5).mean()
    df["MA5"] = ma5

    df = df.fillna(0)  # 결측값(NaN을 0으로 모두 치환)
    print(df)


if __name__ == "__main__":
    main()