# ---------------------------------------------------------------------
# [실습1] 2개의 정수를 입력 받은 후 사칙 연산 수행 결과를 반환하는 기능의 함수를 정의하라.
# 함수이름: fourCalc
# 매개변수 : n1, n2
# 변환결과 : 사칙 연산 결과
# ---------------------------------------------------------------------
def fourcalc(n1, n2):
    # print(f'{n1} + {n2} = {n1+n2}')
    # print(f'{n1} - {n2} = {n1-n2}')
    # print(f'{n1} * {n2} = {n1*n2}')
    # print(f'{n1} / {n2} = {n1/n2}')

    return n1+n2, n1-n2, n1*n2, n1/n2 if n2 else '0으로 나눌 수 없음'


print(fourcalc(1,2))
print(fourcalc(1, 0))
print()


# ------------------------------------------------------------------------
# [실습2] 문자열을 16진수 코드값으로 변환 후 변환하는 함수를 정의하라.
# 함수이름: getCode
# 매개변수 : message
# 변환결과 : str
# --------------------------------------------------------------------
def getCode(message):
    '''
    print(f'입력받은 문자열: {message}')
    for x in message:
        print(f'{x} => 16진수: {hex(ord(x))}')
    '''

    ret =''
    for msg in message:
        ret = ret + hex(ord(msg)) + ' '
    return ret

print(getCode('hello python!'))

