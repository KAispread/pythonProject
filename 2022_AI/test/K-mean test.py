import numpy as np

data = np.loadtxt("../K-mean-clustering/iris.csv", delimiter=",", dtype=np.float32, skiprows=1)

sum_data = np.zeros((3, 4))
avg_data = np.zeros((3, 4))
dis_data = np.zeros((3, 4))


def average():
    for z in range(50):
        for a in range(4):
            sum_data[0][a] += data[z][a]

    for z in range(50, 100):
        for a in range(4):
            sum_data[1][a] += data[z][a]

    for z in range(100, 150):
        for a in range(4):
            sum_data[2][a] += data[z][a]

    for i in range(3):
        print("Average Class : ", i)
        for a in range(4):
            avg_data[i][a] = sum_data[i][a] / 50
        print("Average Attributes :: ", avg_data[i][0], avg_data[i][1], avg_data[i][2], avg_data[i][3], "\n")


def dispersion():
    for z in range(50):
        for a in range(4):
            dis_data[0][a] = (data[z][a] - avg_data[0][a]) * (data[z][a] - avg_data[0][a])

    for z in range(50, 100):
        for a in range(4):
            dis_data[1][a] = (data[z][a] - avg_data[0][a]) * (data[z][a] - avg_data[0][a])

    for z in range(100, 150):
        for a in range(4):
            dis_data[2][a] = (data[z][a] - avg_data[0][a]) * (data[z][a] - avg_data[0][a])

    for i in range(3):
        print("dispersion Class : ", i)
        for a in range(4):
            dis_data[i][a] = dis_data[i][a] / 50
        print("dispersion Attributes :: ", dis_data[i][0], dis_data[i][1], dis_data[i][2], dis_data[i][3], "\n")


def distance(a, b):
    dist = (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2]) \
           + (a[3] - b[3]) * (a[3] - b[3])
    return dist


mean = np.array([[4.9, 3.1, 1.5, 0.1], [6.4, 3.2, 4.5, 1.5], [5.8, 2.7, 5.1, 1.9]])
p = np.zeros(4)
d = np.zeros(3)

sum = np.zeros((3, 4))
num = np.zeros(3)

average()
dispersion()

for epoch in range(10):

    for i in range(150):
        p[0] = data[i][0]
        p[1] = data[i][1]
        p[2] = data[i][2]
        p[3] = data[i][3]
        d[0] = distance(mean[0], p)
        d[1] = distance(mean[1], p)
        d[2] = distance(mean[2], p)
        minIdx = np.argmin(d)
        sum[minIdx][0] += p[0]
        sum[minIdx][1] += p[1]
        sum[minIdx][2] += p[2]
        sum[minIdx][3] += p[3]
        num[minIdx] += 1

    for i in range(3):
        if num[i] != 0:
            mean[i][0] = sum[i][0] / num[i]
            mean[i][1] = sum[i][1] / num[i]
            mean[i][2] = sum[i][2] / num[i]
            mean[i][3] = sum[i][3] / num[i]

    print("epoch : ", epoch)
    print("대표 패턴 : \n ", mean)
    print("Num  : ", num, "\n")

    for i in range(3):
        for a in range(4):
            sum[i][a] = 0

        num[i] = 0

result = np.zeros(3)
inserted_flower = np.array([4.2, 3.2, 2.7, 0.8])

for i in range(3):
    result[i] = distance(mean[i], inserted_flower)


mindist = np.argmin(result)


print(" 4번  문제 : ", mindist, "번 클래스와 가깝다.")

