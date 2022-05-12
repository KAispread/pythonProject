import numpy as np


def activation_tlu(out):
    if out > 0.0:
        return 1.0
    return 0.0


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


x = np.array([[1.0, 0.0, 0.0],
              [1.0, 0.0, 1.0],
              [1.0, 1.0, 0.0],
              [1.0, 1.0, 1.0]])
t = np.array([0.0, 0.0, 0.0, 1.0])  # target array 선언

lrate = 0.1

w = np.zeros(3)

w[0] = 0.5
w[1] = 0.2
w[2] = 0.7

for epoch in range(1000):
    print("epoch : ", epoch)
    for i in range(4):
        out = w[0] * x[i][0] + w[1] * x[i][1] + w[2] * x[i][2]
        # b = activation_tlu(out)
        b = sigmoid(out)
        print(t[i], b, out)
        for j in range(3):
            w[j] = w[j] + lrate * (t[i] - b) * x[i][j]
