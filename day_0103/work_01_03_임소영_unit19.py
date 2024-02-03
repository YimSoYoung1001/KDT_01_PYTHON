# ==============================================
# UNIT 19
# ==============================================

# 연습문제 19.5
for i in range(5):
    for j in range(5):
        if i <= j:
            print('*', end='')
        else:
            print(' ',end='')
    print()
# 세로값을 i, 가로값을 j라고 했을 때
# j 값이 i보다 크거나 같을떄 *을 표기
# 그렇지 않은 경우라면 빈칸으로 표시


# 심사문제 19.6
num = input()
if num.isdigit():
    num = int(num)
    for x in range(num):
        print(' ' * ((num - 1) - x), end='')
        print('*' * (2 * x + 1), end='')
        print(' ' * ((num - 1) - x), end='')
        print()

else:
    print('잘못된 입력값입니다. 정수를 입력.')

