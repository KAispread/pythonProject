import numpy as np
import math as m


def act_tlu(out):
    if (out > 0.0):
        return 1.0
    return 0.0


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


lrate = 0.1
INDIM = 10  # INPUT Layer - 10
H1DIM = 5  # HIDDEN Layer - 5   Hidden layer은 정하기 나름, 정해진 건 없다.
OUTDIM = 2  # OUTPUT Layer - 2

# INPUT 10 (x0 = 1.0 포함)
x = np.array([[1.0, 1.0, 1.0, 1.0,
               1.0, 1.0, 0.0,
               1.0, 1.0, 0.0],  # T
              [1.0, 1.0, 1.0, 1.0,
               1.0, 0.0, 0.0,
               1.0, 1.0, 1.0]])  # C

# OUTPUT 2
t = np.array([[1.0, 0.0], [0.0, 1.0]])

w1 = np.zeros([H1DIM, INDIM])
for i in range(H1DIM):
    for j in range(INDIM):
        w1[i][j] = np.random.rand()

w2 = np.zeros([OUTDIM, H1DIM])
for i in range(OUTDIM):
    for j in range(H1DIM):
        w2[i][j] = np.random.rand()

print(w1)
print(w2)

y1 = np.zeros(H1DIM)  # HIDDEN1 Layer의 결과 5개
y2 = np.zeros(OUTDIM)  # OUTPUT Layer의 결과 2개

d1 = np.zeros(H1DIM)  # HIDDEN1 Layer의 ERROR
d2 = np.zeros(OUTDIM)  # OUTPUT Layer의 ERROR

for epoch in range(1000):
    if (epoch % 10) == 0:
        print("epoch : ", epoch)

    for p in range(2):

        # 입력층에서 은닉층까지 weight를 먹였을 때 결과값
        for i in range(H1DIM):
            out = 0.0
            for j in range(INDIM):
                out += w1[i][j] * x[p][j]
            y1[i] = sigmoid(out)

        for i in range(OUTDIM):
            out = 0.0
            for j in range(H1DIM):
                out += w2[i][j] * y1[j]
            y2[i] = sigmoid(out)

        # Layer2 (은닉 - 출력층) error 계산
        for i in range(OUTDIM):
            d2[i] = (t[p][i] - y2[i])

        # Layer1 (입력 - 은닉층) error 계산
        for i in range(H1DIM):
            for j in range(OUTDIM):
                d1[i] = d2[j] * w2[j][i]

        # Weight Adjustment for Layer-2
        for i in range(OUTDIM):
            for j in range(H1DIM):
                w2[i][j] += lrate * d2[i] * (y2[i] * (1 - y2[i])) * y1[j]

        # Weight Adjustment for Layer-1
        for i in range(H1DIM):
            for j in range(INDIM):
                w1[i][j] += lrate * d1[i] * (y1[i] * (1 - y1[i])) * x[p][j]

        if epoch % 10 == 0:
            print("%7.2f" % t[p], "%7.2f" % y2[p])