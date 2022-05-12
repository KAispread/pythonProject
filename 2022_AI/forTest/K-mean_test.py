import numpy as np

irisData = np.loadtxt("../K-mean-clustering/iris.csv", delimiter=",", dtype=np.float32, skiprows=1)


def get_distance(a, b):
    dist = (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2]) + (
            a[3] - b[3]) * (a[3] - b[3])
    return dist


mean_vector = np.array([[4.9, 3.1, 1.5, 0.1], [5.7, 2.9, 4.2, 1.3], [6.7, 3.1, 5.6, 2.4]])
attributes = np.zeros(4)
distance = np.zeros(3)

sum = np.zeros((3, 4))
num = np.zeros(3)

print(mean_vector[0][0])
print(mean_vector[1])
print(mean_vector[2])

for epoch in range(10):
    for i in range(150):
        attributes[0] = irisData[i][0]
        attributes[1] = irisData[i][1]
        attributes[2] = irisData[i][2]
        attributes[3] = irisData[i][3]
        distance[0] = get_distance(mean_vector[0], attributes)
        distance[1] = get_distance(mean_vector[1], attributes)
        distance[2] = get_distance(mean_vector[2], attributes)
        minClass = np.argmin(distance)
        sum[minClass][0] += attributes[0]
        sum[minClass][1] += attributes[1]
        sum[minClass][2] += attributes[2]
        sum[minClass][3] += attributes[3]
        num[minClass] += 1

    for a in range(3):
        if num[a] != 0:
            mean_vector[a][0] = sum[a][0] / num[a]
            mean_vector[a][1] = sum[a][1] / num[a]
            mean_vector[a][2] = sum[a][2] / num[a]
            mean_vector[a][3] = sum[a][3] / num[a]

    print("epoch :: ", epoch)
    print("num :: ", num, "\n")

    for a in range(3):
        for b in range(4):
            sum[a][b] = 0
        num[a] = 0
