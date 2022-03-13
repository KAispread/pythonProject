
StringFile = open("과제.txt", 'r')       # 암호화 할 파일 호출
String = StringFile.read()              # 과제.txt를 String에 저장
print("Plain Text : ", String)
String = String.upper()
String = String.replace(" ", "")
StringFile.close()

Table_List = []

def Table_Make1():                          # 암호화 Table 일차원 배열 생성
    for x in String:                        # 암호화 할 문장을 Table_List 리스트에 삽입, 중복되는 값은 삽입하지 않음
        if x not in Table_List:
            Table_List.append(x)

    for i in range(65, 91):                 # 아스키코드로 A ~ Z 까지의 범위
        if chr(i) not in Table_List:        # Key값 리스트에 없는 알파벳을 추가
            Table_List.append(chr(i))

def Table_Make2():                          # 암호화 Table 5 x 5 배열 생성
    global Security_Table
    def Table(x, y, First):
        return [[First for i in range(x)] for j in range(y)]

    a = 0
    Security_Table = Table(5, 5, 0)         # 5 x 5 배열의 암호화 테이블 생성
    for i in range(0, 5):                   # 암호화 테이블에 플레이페어 암호화의 키값을 삽입
        for j in range(0, 5):
            Security_Table[i][j] = Table_List[a]
            a = a + 1

def Index(c):                                               # 주어진 텍스트의 알파벳이 암호화 테이블에서 어느 위치인지 인덱스를 저장해주는 함수
    Lo = []
    for i, j in enumerate(Security_Table):                  # index와 값을 반환
        for k, l in enumerate(j):
            if c == l:
                Lo.append(i)                                # 행 인덱스 삽입
                Lo.append(k)                                # 열 인덱스 삽입
                return Lo

def Encrypt():                                              # 암호화 함수
    i = 0                                                   # while 문을 체크하기 위한 'i' index 생성
    StringText = str(String)
    StringText = StringText.upper()
    StringText = StringText.replace(" ", "")

    for s in range(0, len(StringText) + 1, 2):              # 평문을 2개씩 묶은 문자쌍 생성
        if s < len(StringText) - 1:                         # 마지막 문자를 걸러주기위한 if문
            if StringText[s] == StringText[s + 1]:          # 중복되는 문자 쌍에 'X' 추가
                StringText = StringText[:s + 1] + 'X' + StringText[s + 1:]
    if len(StringText) % 2 != 0:
        StringText = StringText[:] + 'X'                    # 마지막에 하나 남은 문자에 'X' 추가

    print("Encryption :", end=" ")
    while i < len(StringText):
        ID1 = []                                            # 두 문자쌍 중 '첫번째 글자' 인덱스
        ID2 = []                                            # 두 문자쌍 중 '두번째 글자' 인덱스
        ID1 = Index(StringText[i])
        ID2 = Index(StringText[i + 1])

        if ID1[1] == ID2[1]:                                 # 열이 같은 경우, 열의 값은 그대로 두고, 행의 값을 한칸씩 뒤로 미룬다. 행의 크기가 5이므로 나누기 5
            print("{}{}".format(Security_Table[(ID1[0] + 1) % 5][ID1[1]], Security_Table[(ID2[0] + 1) % 5][ID2[1]]), end=' ')
        elif ID1[0] == ID2[0]:                               # 행이 같은 경우, 행의 값은 그대로 두고, 열의 값을 한칸씩 뒤로 미룬다. 열의 크기가 5이므로 나누기 5
            print("{}{}".format(Security_Table[ID1[0]][(ID1[1] + 1) % 5], Security_Table[ID2[0]][(ID2[1] + 1) % 5]), end=' ')
        else:                                                #첫번째 글자의 행과 두번째 글자의 열에 있는 문자로 치환, 첫번째 글자의 열과 두번째 글자의 행에 있는 문자로 치환
            print("{}{}".format(Security_Table[ID1[0]][ID2[1]], Security_Table[ID2[0]][ID1[1]]), end=' ')
        i = i + 2

Table_Make1()
Table_Make2()
print('---Encryption Table---', end='\n')
for i in range(0, 5):
    for x in range(0, 5):
        print(Security_Table[i][x], end="\t")
    print('\n')
print('---Encryption Table---', end='\n')
Encrypt()