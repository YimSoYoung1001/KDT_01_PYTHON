# work_01_05_unit26_임소영

# 연습문제 26.8
# 1 부터 100 까지의 숫자 중 3과 5의 공배수를 세트 형태로 출력

a = {x for x in range(1, 101) if x % 3 == 0}
b = {x for x in range(1, 101) if x % 5 == 0}
print(a & b)

# 심사문제 26.9
# 표준입력으로 양의 정수 2개가 입력됨
# 두 숫자의 공약수를 세트 형태로 구한다.
# 최종 결과는 공약수의 합으로 판단

num1, num2 = input().split()

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

a = {x for x in range(1, num1+1) if num1 % x == 0}
b = {y for y in range(1, num2+1) if num2 % y == 0}

divisor = a & b
result = 0
if type(divisor) == set:
    result = sum(divisor)

print(result)
