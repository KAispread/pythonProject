import re                           # re.sub 를 사용하기 위함
import random                       # random.shuffle 명령어를 사용하기 위함

Key_Alphabet = []                   # 영문 키값을 저장 할 리스트
Key_Number = []                     # 숫자 키값을 저장 할 리스트
Alphabet_frequency = []             # 알파벳 빈도수를 기록 할 리스트
Alphabet_origin = []                # A~Z까지의 기본 알파벳 순서를 저장할 리스트

StringFile = open("과제.txt", 'r')   # 암호화 할 파일 호출
StringText = StringFile.read()      # 과제.txt를 StringText에 저장
StringFile.close()

def Origin_Al():                    # A부터 Z까지 알파벳을 Origin_Al 리스트에 삽입
    for a in range(65, 91):
        Alphabet_origin.append(chr(a))

def Number_Al():                    # 숫자를 암호화 할 아스키코드 15 ~ 25 까지의 값을 Number_Al 리스트에 삽입
    for a in range(15, 25):
        Key_Number.append(chr(a))

class Exe:                                              # 암호화에 필요한 함수를 포함하는 클래스 'Exe'
    def __init__(self, text):                           # __init__ 은 # 초기화 메서드
        self.text = text

    def printcount(self):                               # 알파벳에 따른 빈도수 측정 함수
        Text = self.text.lower()                        # 텍스트를 소문자로 치환
        for i in range(97, 123):
            cnt = Text.count(chr(i))
            Alphabet_frequency.append({'ALpha': chr(i), 'frequency': cnt})   # ALpha엔 문자, frequency엔 빈도수 저장

        Alphabet_frequency.sort(key=lambda x: x['frequency'], reverse=True)  # 알파벳 순서를 빈도에 따라 정렬
        for i in Alphabet_frequency:                                         # 빈도수에 따라 알파벳만 따로 분리
            Key_Alphabet.append(i['ALpha'])

    def Encryption(self):                               # 암호화 함수
        text = self.text.upper()                        # 한 문자가 여러번 치환되는 것을 막기 위해 기존 텍스트를 대문자로 치환
        for b in range(0, 10):                          # 숫자 암호화
            SeN = chr(48+b)                             # 아스키 코드 48은 '0'이다, 0부터 9까지의 숫자를 변수 SeN에 저장
            BeN = str(Key_Number[b])
            text = text.replace(SeN, BeN)

        for b in range(0, 26):                          # 알파벳 암호화
            s1 = str(Key_Alphabet[b])
            b1 = str(Alphabet_origin[b])
            text = re.sub(b1, s1, text)
        print(text)
        return text

Encryption_exe = Exe(StringText)
print("-------------------------------Alphabet frequency-------------------------------")
Encryption_exe.printcount()                             # 알파벳에 따른 빈도수 측정 함수 실행
Origin_Al()                                             # A ~ Z 까지의 기본 알파벳 리스트 생성
Number_Al()                                             # 특수문자 리스트 생성
random.shuffle(Key_Number)                              # 특수문자 리스트의 순서를 랜덤으로 섞음

Key_A = open("Key_A File.txt", 'w')                     # Key_A File.txt 파일에 키값 저장
for x in Key_Alphabet:
    A_K = str(x)
    Key_A.write(A_K)
Key_A.close()

Key_N = open("Key_N File.txt", 'w')                     # Key_N File.txt 파일에 키값 저장
for x in Key_Number:
    N_K = str(ord(x))                                   # 숫자 키값을 아스키 코드 값인 상수로 변환하여 파일에 저장
    Key_N.write(N_K)
Key_N.close()

print("Alphabet Key       : ", Key_Alphabet)
print("Alphabetical Order : ", Alphabet_origin)
print("Number Key         : ", Key_Number)
for x in Alphabet_frequency:
    print(x, end="\n")

print("---------------------------------Encryption Text---------------------------------")
f = open("Encrypt_Text.txt", 'w')                       # Encrypt_Text.txt 파일에 암호화된 텍스트 저장
f.write(Encryption_exe.Encryption())
f.close()

print("--------------------------------------EndP---------------------------------------")