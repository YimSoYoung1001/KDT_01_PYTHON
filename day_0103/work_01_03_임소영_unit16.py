#work_01_03_임소영_unit 16

# ==============================================
# UNIT 16
# ==============================================

# 연습문제 16.5
x = [49, -17, 25, 102, 8, 62, 21]

for value in x :
    print(value*10, end=' ')

# 심사문제 16.6
num = input()

if num.isdigit() :
    num = int(num)
    for i in range(1,10):
    print(f'{num} * {i} = {num * i}')
else:
    print('잘못된 입력 값입니다.')


