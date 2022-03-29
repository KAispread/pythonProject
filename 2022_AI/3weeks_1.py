# 2017E7024 이기우

import numpy as np
data = np.loadtxt("iris.csv", delimiter=",", dtype=int)
column = 3
row = int(data.size / column)

column_avg = {}
column_dispersion = {}

for a in range(0, column):  # 평균을 구하는 반복문
    avg = 0
    Sum = 0
    for b in range(0, row):
        Sum += data[b][a]
    avg = Sum / row
    column_avg[a] = avg

for c in range(0, column):  # 분산을 구하는 반복문
    D_Sum = 0
    for d in range(0, row):
        D_buffer = column_avg[c] - data[d][c]
        D_buffer *= D_buffer
        D_Sum += D_buffer
    column_dispersion[c] = round((D_Sum / row), 2)


print("First_column - Average = " + str(column_avg[0]))
print("Second_column - Average = " + str(column_avg[1]))
print("Third_column - Average = " + str(column_avg[2]))
print("")
print("First_column - Dispersion = " + str(column_dispersion[0]))
print("Second_column - Dispersion = " + str(column_dispersion[1]))
print("Third_column - Dispersion = " + str(column_dispersion[2]))
