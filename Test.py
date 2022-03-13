# ########################################################
# 3주차
print('''zHello''')
print(1, -1, 10.040, 12315)

data = "Kai", '2017E7024'
print(data * 10)

data2 = "Kai" + '2017E7024 '
print(data2 * 10)

# ########################################################
# 4주차

# 변수는 초기화하여 사용한다.
x = 1
y = 2
x = x + 1
y = y + 3

a = b = c = 1
a, b = 1, 2    # a = 1 , b = 2

a, b = b, a    # Swap 이 가능

a = b          # a와 b의 값이 바뀜
print(a, type(a))

list_data = [1, 2, 3]               # 중요
bool_data = True
tuple_data = (1, 2, 3)      # 튜플 안의 값이 변경 불가
set_data = {2, 3, 1}
dict_data = {0: False, 1: True}     # 중요

name = input("첫 번째 이름 : ")

x = int(input("Number : "))         # 'input' 을 통해 받는 값은 문자열 형식 / 캐스트 연산 필요

x1 = "3.14"
x2 = float(x1)
x3 = int(x2)
x4 = str(x3)
print(x1, x2, x3, x4)

# ########################################################
# 5주차

ad = 6 / 4          # 1.5
ae = 6 // 4         # 1

r = 345
pi = 3.141592
area = r * r * pi

print(area)

time = int(input("시간 입력 : "))
min = (time//60)
sec = (time%60)

print(str(min) +"분" + str(sec) + "초")



