import numpy as np


def activation_tlu(out):
    if out > 0.0:
        return 1.0
    return 0.0


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


x = np.array([[1.0, 1.0, 1.0,     # T
              0.1, 1.0, 0.1,
              0.1, 1.0, 0.1],

              [1.0, 1.0, 1.0,
               1.0, 0.1, 0.1,
               1.0, 1.0, 1.0]])   # C
t = np.array([1.0, 0.0], [0.0, 1.0])  # target array 선언


lrate = 0.01


w = np.zeros((2, 9))  # w[1][a]는 A 클래스 weight w[2][a]는 B 클래스 weight
out = np.zeros(2)
y = np.zeros(2)

for i in range(2):
    for j in range(9):
        w[i][j] = np.random.rand()  # 2행 9열의 랜덤값 .rand는 0 ~ 1 사이의 랜덤값

for epoch in range(1000):
    print("epoch : ", epoch)
    for p in range(2):
        for i in range(2):
            for j in range(9):
                out[i] += w[i][j] * x[p][j]

        y[i] = sigmoid(out[i])
        print(t[i], y, out)
        for i in range(2):
            for j in range(9):
                w[i][j] = w[i][j] + lrate * (t[p][i] - y[i]) * y[i] * (1-y[i]) * x[p][j]

        print(y)

