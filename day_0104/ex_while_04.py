# -------------------------------------------------------------------
# continue => 계속해서 ~
# - 키워드 아래 코드 실행 안됨
# - 반복 상단으로 이동
# -------------------------------------------------------------------
# 1~30으로 구성된 리스트를 생성하세요.

numList = list(range(1, 31))

# 리스트에 요소 중에서 짝수인 경우만 화면에 출력해주세요.
# print(numList[0])
# print(numList[1])
#    ...
# print(numList[28])
# print(numList[29])

for data in numList:
    if not data % 2:
        print(data)

for data in numList:
    if data%2:         # True이면 홀수임
        continue
    print(data)

# while ==============================================================
numList = list(range(1, 31))

idx = 0
while idx < 30:
    if numList[idx] % 2  == 0 :
        print(f'{idx}번째 요소 값: {numList[idx]}')
    idx += 1



numList = list(range(1, 31))

idx = -1
while idx < 29:  #29가 가능하도록 설정한다면 와일문 안에서 30번 인덱스라 out of range ERROR
    idx += 1
    if numList[idx] % 2:
        continue
    print(f'{idx}번째 요소 값: {numList[idx]}')
