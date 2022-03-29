#2017E7024 이기우

Sum = 0

for i in range(1, 11):
    number = int(input("10개의 숫자를 입력하세요 (" + str(i) + "/10) : "))
    Sum += number

print("입력된 10개의 숫자 합은 " + str(Sum) + "입니다.")
