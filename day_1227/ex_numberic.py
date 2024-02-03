'''
수치 데이터 살펴보기
- 정수 => class int : 양수, 0, 음수
- 실수 => class float : 소수점 존재
- 복소수 => class complex
'''

#-----------------------------------
# [실습] 2개 정수를 입력받기
# => input() : 함수 2개 사용
# => str -> int 타입 캐스팅
#-----------------------------------

num1 = int(input("첫번째 정수를 입력하세요: "))
num2 = int(input("두번째 정수를 입력하세요: "))

# 비교연산 결과 출력 --------------------
# [ 출력 ] 10 > 3 => True

print(f'{num2} > {num1} => {bool(num2>num1)}')
print("%d>%d => %s" %(num1, num2, num1>num2))
print("%d>%d <= %s" %(num1, num2, num1<=num2))
print("%d != %d => %s" %(num1, num2, num1 != num2))