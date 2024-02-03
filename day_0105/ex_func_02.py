# -------------------------------------------------------------------------
# 다양한 함수의 형태 - (1) 기본
# -------------------------------------------------------------------------
# 함수 기능 : 팩토리얼을 계산 후 계산 결과를 반환해주는 기능
#            팩토리얼이란?  3! = 3 * 2 * 1
# 함수 이름 : factorial
# 매개 변수 : num
# 반 환 값 : num에서 1까지 곱한 값
# -------------------------------------------------------------------------
def factorial_my(num):
    original = 1
    if num == 0:
        print(f'0! = 1')

    elif num > 0:
        for i in range(num, 0, -1):
            original = original * i

            #if i = 1:
            # 근데 그 연산 과정을 보여주고 싶단말이지,,, 예를 들면 3!= 3 * 2 * 1 (1번만)

        return original
        return result

    else:
        print('0이상의 정수를 입력하세요.')

print(factorial_my(3))
print()

# 강사님 답 --------------------
def factorial(x):
    ret = 1    #결과 저장 변수
    if x:
        for n in range(x,0,-1):  ret *= n
    # else를 따로 적지 않아도 0이면 false니까 원래 결과저장변수인 ret = 1 이 나옴
    return  ret

print(factorial(3))
print()


# -------------------------------------------------------------------------
# 함수 기능 : 팩토리얼을 계산 후 계산 결과를 아래의 형태로 반환해주는 기능
#            예시 결과   3! = 3 * 2 * 1
# 함수 이름 : factorial2
# 매개 변수 : x
# 반 환 값 : 계산 str
# -------------------------------------------------------------------------
def factorial2(x):
    ret = 1    #결과 저장 변수
    calc = ""  #cal는 빈 문자열이라고 설정함
    if x:
        for n in range(x,0,-1):
            ret *= n

        for k in range(x,1, -1):
            # k = str(k)
            # calc = calc + k + '*'
            calc = calc + str(k) + ('*' if n != 1 else ' = ')
        #calc = calc + '1'
        print(f'{x}! : {calc} = {ret}')

    return  ret

print(factorial2(3))
print()

# 위의 내용은 1번만 연산과정을 나온거
# 만약 각 루프 돌때마다 연산과정을 보고싶다면?
def factorial2_2(x):
    strRet = f'{x}! = '
    intRet = 1
    if x:
        for n in range(x, 0, -1):
            intRet = intRet * n
            strRet = strRet + str(n)
            strRet = strRet + (' * ' if n != 1 else ' = ')
            #print(strRet, intRet) 이거를 주석처리 안하면 각 결과값을 볼수있다. 아니면 그냥 최종 연산과정만 ㅇㅇ

    return strRet + str(intRet)

print(factorial2_2(5))
print()