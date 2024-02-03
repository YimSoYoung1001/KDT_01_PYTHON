# 15장 work_elif_임소영

# 15.3 연습문제
x = int(input())

if 11<= x <= 20 :
    print('11~20')
elif 21<= x <= 30 :
    print('21~30')
else:
    print('아무것도 해당하지 않음')


# 15.4 심사문제

age = int(input('현재 만 나이는? '))
balance = 9000
if 7 <= age <= 12:
    bus = 650
elif 13 <= age <= 18:
    bus = 1050
elif age >= 19:
    bus = 1250

print(balance-bus)