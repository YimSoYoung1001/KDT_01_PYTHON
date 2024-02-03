# 1~100 범위에서 2의 배수에 해당하는 정수로 리스트 생성
result = list(range(2,101,2))

# "24681012 ... 100"
result = str(result)
print(result)  #이르케하면 대괄호부터 0번 인덱스
print(result[0], result[-6], result[-2], result[-1])

# int ==> str 형변환 ------------------------------------------------------

# ------------------------------------------------------------------------
# 시퀀스 데이터 타입에서 원소/요소를 하나씩 해서 반복코드 수행 => for in 반복문
# ------------------------------------------------------------------------

strNum = ''
for num in result:       # result 속 첫번째 요소를 num에 넣어준다.
    #str(num)             # 첫번째 요소가 넣어진 num에 str 함수가 적용된다.
    strNum = strNum + str(num)
print(f'strNum => {type(strNum)} \n{strNum}')
# result는 원본그대로 유지됨

print()
# ---------------------------------------------------------------------
# 리스트 안에 모든 원소를 str 타입으로 변환해서 저장
# ---------------------------------------------------------------------
# 데이터의 인덱스 범위 => 0 ~ len(data)-1
result = list(range(2,101,2))
#range(len(result))  #range의 end 값은 +1 하니까

for idx in range(len(result)):
    result[idx] = str(result[idx])
print(f'result => {result}')

