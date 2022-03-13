import re

crc_code = 0
crc = str(input("다항 코드를 입력해주세요. [ex) x3+x2+x1+1]   =  "))
tas = crc.find("x1")

if tas > 0:
    crc_code += 10
crc = crc.replace("x1", "")

list1 = re.findall('\d+', crc)

for i in range(0, len(list1)):
    num = 1
    for a in range(0, int(list1[i])):
        if int(list1[i]) == 1:
            continue
        num *= 10

    crc_code += num

print(crc_code)
