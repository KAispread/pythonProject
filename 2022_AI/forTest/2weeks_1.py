#2017E7024 이기우
import numpy as np

w = np.zeros(3)
w[0] = np.random.uniform(0.01, 0.2)
w[1] = np.random.uniform(0.01, 0.2)
w[2] = np.random.uniform(0.01, 0.2)


for i in range(3):
    print(w[i])


