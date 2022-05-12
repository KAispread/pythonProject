import numpy as np
import math as m


def act_tlu(out):
    if (out > 0.0):
        return 1.0
    return 0.0


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))

lrate = 0.1
INDIM = 3
H1DIM = 3
OUTDIM = 1

x = np.array([[1.0, 0.1, 0.1],
              [1.0, 0.1, 1.0],
              [1.0, 1.0, 0.1],
              [1.0, 1.0, 1.0]])
t = np.array([0.0, 1.0, 1.0, 0.0])


w1 = np.zeros([H1DIM, INDIM])
for i in range(H1DIM):
    for j in range(INDIM):
        w1[i][j] = np.random.rand()

w2 = np.zeros(H1DIM)
for i in range(H1DIM):
    w2[i] = np.random.rand()


print(w1)
print(w2)


y1 = np.zeros(H1DIM)            # OUTPUT
y2 = 0.0


d1 = np.zeros(H1DIM)            # ERROR
d2 = 0.0


for epoch in range(1000):
    if (epoch % 10) == 0:
        print("epoch : ", epoch)
    for p in range(4):
        for i in range(H1DIM):    # 입력층에서 은닉층까지 먹이는 과정
            out = 0.0
            for j in range(INDIM):
                out += w1[i][j] * x[p][j]
            y1[i] = sigmoid(out)

        out = 0.0

        for i in range(H1DIM):    # 은닉층에서 출력층까지 먹이는 과정
            out += w2[i] * y1[i]
        y2 = sigmoid(out)

        # Layer2 (은닉 - 출력층) error 계산
        d2 = (t[p] - y2)

        # Layer1 (입력 - 은닉층) error 계산
        for i in range(H1DIM):
            d1[i] = d2 * w2[i]

        # Weight Adjustment for Layer-2
        for i in range(H1DIM):
            w2[i] += lrate * d2 * (y2*(1 - y2)) * y1[i]

        # Weight Adjustment for Layer-1
        for i in range(H1DIM):
            for j in range(INDIM):
                w1[i][j] += lrate * d1[i] * (y1[i] * (1 - y1[i])) * x[p][j]

        # if epoch % 10 == 0:

