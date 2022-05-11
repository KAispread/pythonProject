# 2017E7024  이기우
import numpy as np


def x_avg_return():                   # x의 평균 리턴
    sum = 0
    avg = 0
    for i in range(5):
        sum += data[i][0]

    return sum / 5


def y_avg_return():                   # y의 평균 리턴
    sum = 0
    avg = 0
    for i in range(5):
        sum += data[i][1]

    return sum / 5


def deviation_mul(avg_x, avg_y):      # 편차 곱
    x_deviation = 0.0
    y_deviation = 0.0
    deviation_multiply = 0.0

    for i in range(5):
        x_deviation = data[i][0] - avg_x
        y_deviation = data[i][1] - avg_y

        deviation_multiply += (x_deviation * y_deviation)

    return round(deviation_multiply, 3)


def return_b1(avg_x, avg_y):      # b1 구하기
    x_deviation = 0.0
    x_deviation_square = 0.0

    for i in range(5):      # 편차 제곱 구하기
        x_deviation = data[i][0] - avg_x
        x_deviation_square += (x_deviation * x_deviation)

    deviation_mul_return = deviation_mul(avg_x, avg_y)
    return deviation_mul_return / x_deviation_square


def return_b0(avg_x, avg_y, b1):        # b0 구하기
    b0 = 0.0
    b0 = avg_y - (b1 * avg_x)
    return b0


def linear_return_analysis(b0, b1, x):  # 최종 식
    result = 0.0
    result = b0 + (b1 * x)
    return round(result, 3)


data = np.array([[163, 71],
                [137, 67],
                [78, 67],
                [97, 77],
                [110, 120]])

Avg_x = 0.0
Avg_y = 0.0
b1 = 0.0
b0 = 0.0

Avg_x = x_avg_return()
Avg_y = y_avg_return()

b1 = return_b1(Avg_x, Avg_y)
b0 = return_b0(Avg_x, Avg_y, b1)

print("거리가 100 일 경우 집 가격은 :: " + str(linear_return_analysis(b0, b1, 100)))

