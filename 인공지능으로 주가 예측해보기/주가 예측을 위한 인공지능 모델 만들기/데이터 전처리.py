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

    # 가격의 중간값 계산하기
    high_prices = df["High"].values
    low_prices = df["Low"].values
    mid_prices = (high_prices + low_prices) / 2

    # 중간 값 요소 추가하기
    df["Mid"] = mid_prices

    # 이동평균값 계산하기
    ma5 = df["Adj Close"].rolling(window=5).mean()
    df["MA5"] = ma5

    df = df.fillna(0)  # 결측값(NaN을 0으로 모두 치환)

    """
    데이터 전처리
    """
    # Date 변수를 제거합니다.
    df = df.drop("Date", axis=1)

    # 데이터 스케일링 (preprocessing)
    min_max_scaler = MinMaxScaler()
    fitted = min_max_scaler.fit(df)

    output = min_max_scaler.transform(df)
    output = pd.DataFrame(output, columns=df.columns, index=list(df.index.values))
    print(output.head())


if __name__ == "__main__":
    main()