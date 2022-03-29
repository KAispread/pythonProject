import numpy as np

data = np.loadtxt("iris.csv", delimiter=",", dtype=np.float32, skiprows=1)

# 데이터의 4가지 속성을 통해 데이터를 군집화한다.
# 속성이 n개 라면, n차원 공간상에서의 두 점사이의 거리를 측정(데이터간 유사도를 측정).
# 대표 벡터와 점과 점 사이의 거리 공식을 통해 데이터를 K개의 그룹으로 나눈다.
"""
1. 초기화
2. Grouping
3. 그룹의 평균으로 대표 패턴 변경.
4. 2~4번을 반복
"""
average_data = np.array([   # 임의의 대표 패턴 생성.
    [2.7, 1.1],
    [1.7, 2.7],
    [4.2, 3.5]
])

sum = np.zeros((3, 2))      # 대표 패턴을 구하기 위한 데이터의 합 저장 버퍼
num = np.zeros(3)           # count buffer

for epoch in range(5):      # 반복 횟수를 5로 설정
    # Step 2 : Grouping
    for i in range(0, 150):
        minDistClass = MinDistance(average_data, data[i])  # 대표값과 최소거리를 측정하여 해당 그룹의 인덱스를 반환
        sum[minDistClass] += minDistClass
        num[minDistClass] += 1

    # Step 3 : Adjust
    average_data[0] = sum[0] / num[0]
    average_data[1] = sum[1] / num[1]
    average_data[2] = sum[2] / num[2]


