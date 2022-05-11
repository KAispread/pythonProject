# 2017E7024 이기우 - 델타 규칙을 사용한 신경망 학습
import numpy as np

x = np.array([[1.0, 0.0, 0.0],
              [1.0, 0.0, 1.0],
              [1.0, 1.0, 0.0],
              [1.0, 1.0, 1.0]])
# p1[w1, w2, w3] ~ p4 까지의 값 지정

t = np.array([0.0, 0.0, 0.0, 1.0])
# 각 패턴에 대한 Target 지정 (And gate)

# t = np.array([0.0, 1.0, 1.0, 1.0])
# 각 패턴에 대한 Target 지정 (OR gate)

lrate = 0.1
# learning Rate 값 지정 / 값이 작을 수록 학습이 느리게 됨.

w = np.zeros(3)
# w1 ~ 3까지의 값이 들어갈 버퍼

w[0] = 0.5
w[1] = 0.2
w[2] = 0.7


def act_tlu(out):
    if out > 0.0:
        return 1.0
    return 0.0


for epoch in range(10):  # 사이클 반복 횟수 10회
    print("epoch ", epoch)
    for i in range(4):
        out = w[0] * x[i][0] + w[1] * x[i][1] + w[2] * x[i][2]
        b = act_tlu(out)  # TLU 작업 진행 (1 or 0)
        print("target : ", t[i], "/ result : ", b)
        # print(w)

        for j in range(3):
            w[j] = w[j] + lrate * (t[i] - b) * x[i][j]
