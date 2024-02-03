# ----------------------------------------------------------------------------
# 반복문 - 2. while 반복문
# - 반복의 횟수 정해지지 않은 경우
# ----------------------------------------------------------------------------
# [요청] 사용자가 'x' 입력 전까지 입력 받은 데이터 저장해주세요.
# => 몇 번 입력할지 알수 없음 => 무한 입력 받기
# => 종료 조건 ==> 사용자가 'x' 입력

while True:          # 안에서 어떤 정지 조건이 되지 않는 무한 반복
    data = input('저장하고 싶은 데이터 입력 (종료 X) : ')

    # 종료 검사
    # => break: 키워드가 있는 부분에서 바로 반복 종료, 아래 코드 실행 안됨

    #if data == 'x' or data == 'X':
    if data in ('x', 'X'):
        break
    print('OK')    #x가 입력되는 순간 break를 만나서 남은 while문들은 실행안하고 반복문 밖으로 나감

print("프로그램 종료")



# ----------------------------------------------------------------------------
# [요청] 사용자로부터 x/X 입력 전까지 계속 정수를 입력
#       입력 받은 정수만큼 알파벳을 출력
#       출력 원하는 알파벳 수 입력 : 5
#       abcde
#       출력 원하는 알파벳 수 입력 : 1
#       a
#       출력 원하는 알파벳 수 입력 : 10
#       abcdefghij
#       출력 원하는 알파벳 수 입력 : 27
#       abcdefghijklmnopqrstuvwxyz 종료
#       출력 원하는 알파벳 수 입력 : x
#       종료
# ----------------------------------------------------------------------------

'''
오류뜬다,,,ㅜ

while True:
    num = input('출력하고 싶은 알파벳의 수를 입력: ')

    # 무한 입력 반복 종료 조건
    if num in ('x', 'X') :
        print('종료입니다.')
        break     # 즉시 종료
                  # 밑에 else가 있어도 시행되지않음
    num = int(num)
    aCode = ord('a')
    zCode = ord('z')

    while i in range(aCode, zCode +1):
        alphabet = chr(i)  #코드값에 따른 알파벳이 나옴
        print(f"{alphabet},end=''")
        i +=1
        if i == zCode :
            print('종료')
            break
'''


while True:
    count = input("출력 원하는 알파벳 수 : ")
    # 종료 코드
    if count in ('x', 'X'):
        print("프로그램 종료됩니다.")
        break  #가장 가까운 반복문인 while True문을 빠져나감
        
    if count.isdecimal():
        count = int(count)
        aCode = ord('A')
        for value in range(count):
            value += aCode
            print(f'value => {value}, {chr(value)}')
            if value == ord('z'): break
            # break는 반복문과만 상관있다. 가장 가까운 반복문을 즉시 멈추고 나감
            # 여기서 break 걸리면 끊고 나감
            
    else:
        print('정확한 데이터가 아닙니다.')

print('===== 코드 끝 =====')

# ----------------------------------------------------------


isEnd = False           #플래그변수

for n in range(100):
    if isEnd:          #플래그변수 통해 코드가 완전히 종료되기 전 알림메시지 표시함
                       #96번 라인에서 플래그변수가 True가 되었으므로 이 if문이 실시됨
        print("프로그램 종료합니다.")
        break          #그래서 최종적으로 종료 알림메시지 표현 후 완전히 종료됨

    print(f"out -> {n}")

    for n2 in range(100):
        if n2 > 10 :
            isEnd = True
            break # 11이 되는 순간 플래그변수는 True로 되고 안쪽 for문이 닫힘

        print(f"in -> {n2} ===> {n}번째")

# 위 코드를 while문으로 재작성

isEnd = False  # 플래그변수
outNum = 1

while outNum <= 100 :
    # 종료조건
    if isEnd :
        print('프로그램이 종료됨')
        break
    print(f'outNum -> {outNum}') #얘가 전체프로그램종료 멘트 후 나와야 함

    # 내부 while
    inNum = 1
    while inNum <= 100 :

        #내부 종료조건
        if inNum > 10:     #10번 찍고 나면 끝나도록
            print('내부 while문 종료')
            isEnd = True
            #만약 이런 플래그변수가 없다면 내부 while문이 총 100번까지 돈다. outNum =100 까지 ㅇㅇ
            #왜냐, 내부를 빠져나가도 113번 라인에서 다시 변수가 설정되니까
            break

        print(f"inNum -> {inNum} ===> {outNum}번째")
        inNum += 1 #값이 반드시 증가되어야한다!!!!!!!!!!!!!!!!

    outNum += 1 #값이 반드시 증가되어야한다!!!!!!!!!!!!!!!!

