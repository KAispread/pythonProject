import re                                           # re.sub 함수를 사용하기 위함

Key_Alphabet = []                                   # 영문 키값을 저장 할 리스트
Key_Number = []                                     # 숫자 키값을 저장 할 리스트
Key_Number_Real = []                                # 단순 숫자로 저장되어 있는 값을 아스키 문자로 변환하여 저장할 리스트
Alphabet_origin = []                                # A~Z까지의 기본 알파벳 순서를 저장할 리스트

StringFile = open("Encrypt_Text.txt", 'r')          # 암호화된 텍스트 불러오기
StringText = StringFile.read()
StringText = str(StringText)
StringFile.close()

Key_A = open("Key_A File.txt", 'r')                 # 영문 키값 파일 불러오기
KeA = Key_A.read()
for x in KeA:
    Key_Alphabet.append(x)
Key_A.close()

Key_N = open("Key_N File.txt", 'r')                 # 숫자 키값 파일 불러오기
Key_Number = Key_N.read()
Do = 1
for x in range(0,20):                               # 단순숫자로 저장되어 있는 아스키코드를 아스키 문자로 변환하여 리스트에 저장
    if x % 2 == 0:
        Do = int(Key_Number[x])
        Do = Do * 10
    else:
        No = int(Key_Number[x])
        Do = Do + No
        Key_Number_Real.append(chr(Do))
Key_N.close()


def Origin_Al():                                    # A부터 Z까지 알파벳을 Origin_Al 리스트에 삽입
    for a in range(65, 91):
        Alphabet_origin.append(chr(a))

def Decryption(text1):                              # 주어진 파일의 복호화
    for c in range(0, 10):                          # 숫자 복호화
        SdN = chr(48 + c)                           # 아스키 코드 48은 '0', 0부터 9까지의 숫자를 변수 SeN에 저장
        BdN = str(Key_Number_Real[c])
        text1 = re.sub(BdN, SdN, text1)

    for c in range(0, 26):                          # 영문 복호화
        Sd1 = str(Key_Alphabet[c])
        Bd1 = str(Alphabet_origin[c])
        text1 = re.sub(Sd1, Bd1, text1)             # 저장된 리스트 순서대로 알파벳 치환(암호화)
    text1 = text1.lower()                           # 소문자로 치환
    print(text1)
    return text1

Origin_Al()
print("------------------------------------Key Table------------------------------------")
print("Alphabet Key       : ", Key_Alphabet)
print("Alphabetical Order : ", Alphabet_origin)
print("Number Key         : ", Key_Number_Real)
print("---------------------------------Decryption Text---------------------------------")
Decryption(StringText)
print("--------------------------------------EndP---------------------------------------")
