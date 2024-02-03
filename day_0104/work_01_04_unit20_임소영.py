# work_01_04_unit20

# 연습문제 20.7 -----------------------------------------------------------------
#2의 배수이면 fizz    11의 배수이면 buzz     2와 11의 공배수는 fizzbuzz
for i in range(1, 101):
    if (i%2 == 0) and (i%11==0):
        print('FizzBuzz')
    elif i%2 == 0:
        print('Fizz')
    elif i%11 == 0:
        print('Buzz')
    else:
        print(i)


# 심사문제 20.8 -----------------------------------------------------------------
# 5   7      5와7

first, number = map(int, input().split())
i = first

for i in range(first, number + 1):
    if (i % 5 == 0) and (i % 7 == 0):
        print('FizzBuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)