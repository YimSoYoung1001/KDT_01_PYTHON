# work_01_04_unit17

# 연습문제 17.5 ----------------------------------------------------------
'''
이렇게 하면 결과값은 나오지만 문제가 의도한 코드 과정과는 다르다.
i = 2
j = 5
n = 1

while i == 2 or j == 5:
    while n in range (1, 6):
        print(f"{2**n} {6-n}")
        n += 1
'''

i = 2
j = 5

while i <= 32 or j >= 1:
    print(i, j)
    i *= 2
    j -= 1



# 심사문제 17.6    ====>      오류발생,, 정수로만 구성된거 확인 코드 수정 필요
'''
1) 금액을 입력 받음 (이게 원금이 된다)
2) 입력된 정보가 양수의 정수인지 확인되면 integer로 형변환
3) 1회가 찍힐 시 잔금에서 -1350 한 값을 출력 (매번ㅇㅇ)
4) 음수가 될때까지 반복 (while)
5) 음수가 되면 끝남
'''

cash = input(' ')
run = True

while run:
    if cash.isdigit:
        cash = int(cash)
        while cash >= 0:
            print(f'{cash}')
            if cash < 0:
                run = False
                break

            cash -= 1350

    else:
        print(f'입력값은 정수이어야 합니다.')
        break