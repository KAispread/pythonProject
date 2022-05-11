# 2017E7024 이기우

import numpy as np

data = np.loadtxt("./iris.csv", delimiter=",", dtype=np.float32, skiprows=1)

# 데이터의 4가지 속성을 통해 데이터를 군집화한다.
# 속성이 n개 라면, n차원 공간상에서의 두 점사이의 거리를 측정(데이터간 유사도를 측정).
# 대표 벡터와 점과 점 사이의 거리 공식을 통해 데이터를 K개의 그룹으로 나눈다.
"""
1. 초기화
2. Grouping
3. 그룹의 평균으로 대표 패턴 변경.
4. 2~4번을 반복
"""


def distance(a, b):  # 두 점사이의 거리를 구하는 함수
    dist = (a[0] - b[0]) * (a[0] - b[0]) + (a[1] - b[1]) * (a[1] - b[1]) + (a[2] - b[2]) * (a[2] - b[2]) \
        + (a[3] - b[3]) * (a[3] - b[3])
    # 정확한 거리 측정을 위해 루트를 씌워야 하지만 단순 거리비교만 하기 위해 생략
    return dist


mean = np.array([[4.9, 3.1, 1.5, 0.1], [5.7, 2.9, 4.2, 1.3], [6.7, 3.1, 5.6, 2.4]])  # 임의의 표준 데이터 설정
p = np.zeros(4)     # 각 데이터의 속성값을 저장할 배열 속성값이 4개라 배열의 크기도 4.
d = np.zeros(3)     # 대표 벡터와 데이터 값의 거리를 저장, K = 3 이라 배열의 크기도 3.

sum = np.zeros((3, 4))              # 클래스[i]의 속성값을 더함
num = np.zeros(3)                   # 클래스[i]에 데이터가 몇개들어갔는지 저장

for epoch in range(10):
    # Step 2: Grouping
    for i in range(150):
        p[0] = data[i][0]  # x
        p[1] = data[i][1]  # y
        p[2] = data[i][2]  # z
        p[3] = data[i][3]  # w
        d[0] = distance(mean[0], p)
        d[1] = distance(mean[1], p)
        d[2] = distance(mean[2], p)
        minIdx = np.argmin(d)  # 제일 작은 값의 Index 반환
        sum[minIdx][0] += p[0]  # 데이터가 포함되는 그룹의 x 좌표에 값을 더함
        sum[minIdx][1] += p[1]  # 데이터가 포함되는 그룹의 y 좌표에 값을 더함
        sum[minIdx][2] += p[2]  # 데이터가 포함되는 그룹의 z 좌표에 값을 더함
        sum[minIdx][3] += p[3]  # 데이터가 포함되는 그룹의 w 좌표에 값을 더함
        num[minIdx] += 1        # 클래스에 데이터가 몇개 들어갔는지 저장.

    # Step 3: Adjust

    for i in range(3):
        if num[i] != 0:
            mean[i][0] = sum[i][0] / num[i]
            mean[i][1] = sum[i][1] / num[i]
            mean[i][2] = sum[i][2] / num[i]
            mean[i][3] = sum[i][3] / num[i]

    print(epoch)
    print("대표 패턴 :: \n ", mean)
    print("Num  :: ", num, "\n")

    for i in range(3):          # 한 사이클이 끝날때마다 sum과 num 배열을 초기화
        for a in range(4):
            sum[i][a] = 0
        num[i] = 0
