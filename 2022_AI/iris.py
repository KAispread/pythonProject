import numpy as np

data = np.loadtxt("./iris.csv", delimiter=",", dtype=np.float32, skiprows=1)


def Distance(a, b) :   # 두 점사이의 거리를 구하는 함수
    d = (a[0] - b[0])*(a[0] - b[0]) + (a[1] - b[1])*(a[1] - b[1])
    # 정확한 거리 측정을 위해 루트를 씌워야하지만 단순 거리비교만 하기 위해 생략
    return d

mean = np.array([5.2, 4.0], [5.0, 3.3], [4.7, 3.5])                 # 임의의 표준 데이터 설정
p = np.zeros(2)
d = np.zeros(3)

sum = np.zeros((3, 2))
num = np.zeros(3)

for epoch in range(10):
    # Step 2: Grouping
    for i in range(150):
        p[0] = data[i][0]               # x
        p[1] = data[i][1]               # y
        d[0] = Distance(mean[0], p)
        d[1] = Distance(mean[1], p)
        d[2] = Distance(mean[2], p)
        print(p, data[i], mean, d)
        minIdx = np.argmin(d)           # 제일 작은 값의 Index 반환
        sum[minIdx][0] += p[0]          # 데이터가 포함되는 그룹의 x 좌표에 값을 더함
        sum[minIdx][1] += p[1]          # 데이터가 포함되는 그룹의 y 좌표에 값을 더함
        num[minIdx] += 1

    # Step 3: Adjust
    print("Sum && Num :: ", sum, num)

    for i in range(3):
        if num[i] !=0 :
            mean[i][0] = sum[i][0] / num[i]
            mean[i][1] = sum[i][1] / num[i]
    for i in range(3):
        sum[i][0] = sum[i][1] = num[i] = 0

    print("Mean :: ", mean)
    print("Sum  :: ", sum)
    print("Num  :: ", num)