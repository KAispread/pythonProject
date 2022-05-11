import numpy as np


def act_tlu(x):
    if x > 0.0:
        return 1.0
    return 0.0


def act_sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x))


x = np.array([[1.0, 0.0, 0.0],
              [1.0, 0.0, 1.0],
              [1.0, 1.0, 0.0],
              [1.0, 1.0, 1.0]])
t = np.array([0.0, 0.0, 0.0, 1.0])
w = np.zeros(3)

learning_rate = 0.1

for i in range(3):
    w[i] = np.random.rand()

for epoch in range(1000):
    print("epoch 1 :: ", epoch)
    for i in range(4):
        out = w[0] * x[i][0] + w[1] * x[i][1] + w[2] * x[i][2]
        d = act_sigmoid(out)

        print("t :: ", t[i], "d :: ", d)
        for a in range(3):
            w[a] = w[a] + learning_rate * (t[i] - d) * x[i][a]

