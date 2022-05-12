import numpy as np
import math as m


def act_tlu(out):
    if out > 0.0:
        return 1.0
    return 0.0


def sigmoid(x):
    return 1.0 / (1 + m.exp(-x))


lrate = 0.1
INDIM = 10  # INPUT Layer - 10
H1DIM = 5  # HIDDEN Layer - 7   Hidden layer은 정하기 나름, 정해진 건 없다.
H2DIM = 5  # HIDDEN Layer - 5
OUTDIM = 3  # OUTPUT Layer - 3

# INPUT 10 (x0 = 1.0 포함)
x = np.array([[1.0, 1.0, 1.0, 1.0,
               0.0, 1.0, 0.0,
               0.0, 1.0, 0.0],  # T
              [1.0, 1.0, 1.0, 1.0,
               1.0, 0.0, 0.0,
               1.0, 1.0, 1.0],  # C
               [1.0, 1.0, 0.0, 0.0,
               1.0, 0.0, 0.0,
               1.0, 1.0, 1.0]])

# OUTPUT 2
t = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

w1 = np.zeros([H1DIM, INDIM])
for i in range(H1DIM):
    for j in range(INDIM):
        w1[i][j] = np.random.rand()

w2 = np.zeros([H2DIM, H1DIM])
for i in range(H2DIM):
    for j in range(H1DIM):
        w2[i][j] = np.random.rand()

w3 = np.zeros([OUTDIM, H2DIM])
for i in range(OUTDIM):
    for j in range(H2DIM):
        w3[i][j] = np.random.rand()

y1 = np.zeros(H1DIM)  # HIDDEN1 Layer의 결과 7개
y2 = np.zeros(H2DIM)  # HIDDEN1 Layer의 결과 5개
y3 = np.zeros(OUTDIM)  # OUTPUT Layer의 결과 3개

d1 = np.zeros(H1DIM)  # HIDDEN1 Layer의 ERROR
d2 = np.zeros(H2DIM)  # HIDDEN2 Layer의 ERROR
d3 = np.zeros(OUTDIM)  # OUTPUT Layer의 ERROR

for epoch in range(10000):
    if (epoch % 10) == 0:
        print("epoch : ", epoch)

    for p in range(OUTDIM):

        # 입력층에서 은닉층까지 weight를 먹였을 때 결과값
        for i in range(H1DIM):
            out = 0.0
            for j in range(INDIM):
                out += w1[i][j] * x[p][j]
            y1[i] = sigmoid(out)

        for i in range(H2DIM):
            out = 0.0
            for j in range(H1DIM):
                out += w2[i][j] * y1[j]
            y2[i] = sigmoid(out)

        for i in range(OUTDIM):
            out = 0.0
            for j in range(H2DIM):
                out += w3[i][j] * y2[j]
            y3[i] = sigmoid(out)

        # Layer3 (출력층) error 계산
        for i in range(OUTDIM):
            d3[i] = (t[p][i] - y3[i])

        # Layer2 (은닉2) error 계산
        for i in range(H2DIM):
            d2[i] = 0.0
            for j in range(OUTDIM):
                d2[i] += d3[j] * w3[j][i]

        # Layer1 (은닉1) error 계산
        for i in range(H1DIM):
            d1[i] = 0.0
            for j in range(H2DIM):
                d1[i] += d2[j] * w2[j][i]

        # Weight Adjustment for Layer-3
        for i in range(OUTDIM):
            for j in range(H2DIM):
                w3[i][j] += lrate * d3[i] * (y3[i] * (1 - y3[i])) * y2[j]

        # Weight Adjustment for Layer-2
        for i in range(H2DIM):
            for j in range(H1DIM):
                w2[i][j] += lrate * d2[i] * (y2[i] * (1 - y2[i])) * y1[j]

        # Weight Adjustment for Layer-1
        for i in range(H1DIM):
            for j in range(INDIM):
                w1[i][j] += lrate * d1[i] * (y1[i] * (1 - y1[i])) * x[p][j]

        if (epoch % 10) == 0:
            for i in range(3):
              print(t[p][i], "\t", round(y3[i], 2))

xzero = np.array([[1.0, 1.0, 1.0, 1.0,
               1.0, 0.0, 0.0,
               1.0, 0.0, 0.0],
               [1.0, 1.0, 0.0, 0.0,
               1.0, 0.0, 0.0,
               1.0, 1.0, 1.0]])

for i in range(H1DIM):
    out = 0.0
    for j in range(INDIM):
        out += w1[i][j] * xzero[0][j]
    y1[i] = sigmoid(out)

for i in range(H2DIM):
    out = 0.0
    for j in range(H1DIM):
        out += w2[i][j] * y1[j]
    y2[i] = sigmoid(out)

for i in range(OUTDIM):
    out = 0.0
    for j in range(H2DIM):
        out += w3[i][j] * y2[j]
    y3[i] = sigmoid(out)

print("Input ㄱ result is ::")
for i in range(3):
    print(round(y3[i], 2), end="\t")

