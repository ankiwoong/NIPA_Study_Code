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

    # Date 변수를 제거합니다.
    df = df.drop("Date", axis=1)

    # 데이터 스케일링 (preprocessing)
    min_max_scaler = MinMaxScaler()
    fitted = min_max_scaler.fit(df)

    output = min_max_scaler.transform(df)
    output = pd.DataFrame(output, columns=df.columns, index=list(df.index.values))

    # train/test size 설정
    train_size = int(len(output) * 0.6)
    test_size = int(len(output) * 0.3) + train_size

    # train/test 학습 및 라벨 설정#종가를 예측하기 위해 종가를 label로 설정
    train_x = np.array(output[:train_size])
    train_y = np.array(output["Close"][:train_size])
    test_x = np.array(output[train_size:test_size])
    test_y = np.array(output["Close"][train_size:test_size])
    validation_x = np.array(output[test_size:])
    validation_y = np.array(output["Close"][test_size:])

    """
    Keras를 이용한 딥러닝 수행
    
    학습을 위한 모델의 기초 파라미터들을 설정한 후 본격적인 학습을 수행합니다.
    """
    # 학습을 위한 기초 파라메터 설정
    learning_rate = 0.01
    # 전체 데이터셋에 대한 반복 학습 횟수 (Epoch)
    training_cnt = 500
    # 한번에 학습할 데이터의 수 (실행 속도와 관련)
    batch_size = 100
    input_size = 8

    model = Sequential()
    # activation [ tahn, sigmoid, relu etc.]
    model.add(Dense(input_size, activation="tanh", input_shape=(train_x.shape[1],)))
    model.add(Dense(input_size * 3, activation="tanh"))
    model.add(Dense(1, activation="tanh"))

    # activation [ sgd, rmsprop, adam etc.]
    model.compile(optimizer="sgd", loss="mse", metrics=["mae", "mape", "acc"])
    model.summary()
    history = model.fit(
        train_x, train_y, epochs=training_cnt, batch_size=batch_size, verbose=1
    )
    val_mse, val_mae, val_mape, val_acc = model.evaluate(test_x, test_y, verbose=0)

    """
    학습결과 그래프로 확인
    
    """

    plt.title("Error rate graph ")
    plt.plot(history.history["loss"], linestyle="--")
    plt.legend(["loss"], loc="upper left")
    plt.ylabel("loss")
    plt.xlabel("EPoch")

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig(
        "D:\\Code\\Study\\NIPA_Study_Code\\주가 예측을 위한 인공지능 모델 만들기\\result\\plot-1.png"
    )
    # elice_utils.send_image("plot.png")

    pred = model.predict(test_x)

    fig = plt.figure(facecolor="white", figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.plot(test_y, label="True")
    ax.plot(pred, label="Prediction")
    ax.legend()

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig(
        "D:\\Code\\Study\\NIPA_Study_Code\\주가 예측을 위한 인공지능 모델 만들기\\result\\plot-2.png"
    )
    # elice_utils.send_image("plot.png")

    # 최근 500일 정도의 예측 그래프
    pred = model.predict(validation_x)

    fig = plt.figure(facecolor="white", figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.plot(validation_y, label="True")
    ax.plot(pred, label="Prediction")
    ax.legend()

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig(
        "D:\\Code\\Study\\NIPA_Study_Code\\주가 예측을 위한 인공지능 모델 만들기\\result\\plot-3.png"
    )
    # elice_utils.send_image("plot.png")


if __name__ == "__main__":
    main()