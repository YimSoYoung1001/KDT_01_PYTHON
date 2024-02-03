# ----------------------------------------------------------------------------
# 반복문과 내장함수  ==> map()  zip()
# ----------------------------------------------------------------------------
xList = ['1', '3', '5', '7']

# xList 안에 모든 원소를 정수 int로 변환 후 저장해주세요.
# xList[0] = int(xList[0])
# xList[1] = int(xList[1])
# xList[2] = int(xList[2])
# xList[3] = int(xList[3])

for idx in range(len(xList)):
    xList[idx] = int(xList[idx])
print(f'xList => {xList}')


# ----------------------------------------------------------------------------
# 시퀀스 또는 반복이 가능한 객체의 요소/원소에 적용 후 값을 다시 저장해야하는 경우
# 자주 사용되는 기능으로 내장함수로 제공 => map()
# - 문법 : map(함수명, 시퀀스 또는 반복이 가능한 객체)
# ----------------------------------------------------------------------------
# int 요소인 xList를 str 요소로 변환
result = list(map(str, xList))  #각 원소를 str로 바꿔서 map객체로 담음 그걸 list로 형변환
print(f'result => {result}')


# ----------------------------------------------------------------------------
# List 데이터를 dict 데이터로 생성
# ----------------------------------------------------------------------------
x = ['std01', 'std02', 'std03']
y = [90, 10, 99]

# 방법 (1) ---> 기호/부호 {}
xyDict = {}
# xyDict['std01'] = 90
# xyDict['std02'] = 10
# xyDict['std03'] = 99

for idx in range(len(x)):
    xyDict[x[idx]] = y[idx]

# 방법(2) ---> dict() 생성자 함수
xyDict2 = dict()
# xyDict['std01'] = 90
# xyDict['std02'] = 10
# xyDict['std03'] = 99

for idx in range(len(x)):
    xyDict2[x[idx]] = y[idx]

# 방법(3) ---> dict( [ (키, 값), (키, 값) ] ) 생성자 함수
# 교재 145p: 리스트 안에 (키, 값) 형식의 튜플을 나열하고 이를 dict로 딕셔너리 만드는 방법
xy = []
for idx in range(len(x)):
    xy.append(x[idx], y[idx])
print(xy)

xyDict3 = dict(xy)
print(xyDict3)

# 방법(4) ---> dict( [ (키, 값), (키, 값) ] ) 생성자 함수
# by 내장함수 zip()
xyDict4 = dict(zip(x,y))
# - 원래는 반복문으로 하는데 그 대신에 zip 적용해서 만듬
# - zip 통해서 리스트 안에 (키, 값) 형식의 튜플을 만든 후 dict 적용
print(xyDict4)

