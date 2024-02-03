# work_01_05_임소영
# UNIT29 함수 사용하기

# 연습문제 29.7 x를y로 나누었을때 몫과 나머지 출력
# 인출결과 => 몫: 3 , 나머지: 1
x = 10
y = 3
def get_quotient_remainder(x, y):
    return x//y, x%y

quotient, remainder = get_quotient_remainder(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder))



# 심사문제 29.8 사칙연산 함수 만들기
# 표준입력으로 숫자 두개가 입력, 사칙연산 결과 출력, 나눗셈의 결과는 실수여야함.

x, y = map(int,input().split())

def calc(x,y):

    return x+y, x-y, x*y, float(x/y)

a, s, m, d = calc(x,y)
print('덧셈: {0}, 뺼셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a,s,m,d))