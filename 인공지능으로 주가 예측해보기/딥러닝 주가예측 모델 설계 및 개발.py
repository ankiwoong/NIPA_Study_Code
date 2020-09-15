from datetime import datetime  # 날짜와 시간을 쉽게 조작할 수 있게 하는 클래스 제공
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense, SimpleRNN
from tensorflow.keras.layers import LSTM

# from elice_utils import EliceUtils

# elice_utils = EliceUtils()


def main():
    """
    주식 데이터 불러오기
    """
    df = pd.read_csv(
        "D:\\Code\\Study\\NIPA_Study_Code\\인공지능으로 주가 예측해보기\\data\\stock.csv"
    )

    # 데이터 프레임 기본 형 출력
    # row X columns로 이루어진 table 모양

    """
    딥러닝의 입력피쳐 설계
    """
    # 가격의 중간값 계산하기
    high_prices = df["High"].values
    low_prices = df["Low"].values
    mid_prices = (high_prices + low_prices) / 2
    mid_prices

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

    """
    데이터 셋 나누기
    """
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
    LSTM 적용하기
    """
    # 학습을 위한 기초 파라메터 설정
    learning_rate = 0.01
    # 전체 데이터셋에 대한 반복 학습 횟수 (Epoch)
    training_cnt = 100
    # 한번 학습에 사용할 batch size
    batch_size = 200
    # 입력 피쳐의 개수
    input_size = train_x.shape[1]

    time_step = 1

    # reshape into (size(개수), time step, 입력 feature)
    train_x = train_x.reshape(train_x.shape[0], time_step, input_size)
    validation_x = validation_x.reshape(validation_x.shape[0], time_step, input_size)
    test_x = test_x.reshape(test_x.shape[0], time_step, input_size)

    model = Sequential()

    # cell의 개수와 입력 될 데이터의 shape 설정
    model.add(LSTM(512, input_shape=(1, input_size)))

    # Overfitting을 방지하기 위해 Dropout 설정
    model.add(Dropout(0.2))

    # output(target)은 '종가'이기 때문에 1요소 = Dense의 output레이어는 1로 설정
    model.add(Dense(1, activation="tanh"))

    # 오차 및 최적화기 설정
    model.compile(loss="mse", optimizer="rmsprop", metrics=["mae", "mape"])
    model.summary()

    # 학습
    history = model.fit(
        train_x, train_y, epochs=training_cnt, batch_size=batch_size, verbose=1
    )
    val_mse, val_mae, val_mape = model.evaluate(test_x, test_y, verbose=0)

    plt.title("Error rate graph ")
    plt.plot(history.history["loss"], linestyle="--")
    plt.legend(["loss"], loc="upper left")
    plt.ylabel("loss")
    plt.xlabel("EPoch")

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig("D:\\Code\\Study\\NIPA_Study_Code\\인공지능으로 주가 예측해보기\\result\\plot-1.png")
    # elice_utils.send_image("plot.png")

    # 학습이 잘 이루어졌는지 예측
    pred = model.predict(validation_x)

    fig = plt.figure(facecolor="white", figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.plot(validation_y, label="True")
    ax.plot(pred, label="Prediction")
    ax.legend()

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig("D:\\Code\\Study\\NIPA_Study_Code\\인공지능으로 주가 예측해보기\\result\\plot-2.png")
    # elice_utils.send_image("plot.png")

    pred = model.predict(test_x)

    fig = plt.figure(facecolor="white", figsize=(20, 10))
    ax = fig.add_subplot(111)
    ax.plot(test_y, label="True")
    ax.plot(pred, label="Prediction")
    ax.legend()

    # 현재까지 그려진 그래프를 보여줌
    plt.savefig("D:\\Code\\Study\\NIPA_Study_Code\\인공지능으로 주가 예측해보기\\result\\plot-3.png")
    # elice_utils.send_image("plot.png")


if __name__ == "__main__":
    main()