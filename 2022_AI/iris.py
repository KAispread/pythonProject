import numpy as np

data = np.loadtxt("./iris.csv", delimiter=",", dtype=np.float32, skiprows=1)

irisData = {}

irisData[0] = data[:50]
irisData[1] = data[50:100]
irisData[2] = data[100:]

sum = 0.0
cnt = 0

for i in range(0, 50):
    x = irisData[0][i][1]
    print(x)
    sum += x
    cnt += 1
