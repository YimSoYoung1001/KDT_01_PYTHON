# ----------------------------------------------------------------
# for 요소 in 시퀀스/반복 가능한 객체:
# ==> for 인덱스 in range (len(변수)):
# ==> 내장함수 enumerate()
# - (번호, 요소)  묶음으로 반환함!!
# ----------------------------------------------------------------
datas = ['Apple', 'Banana', 'Orange']

#리스트 안에 요소/원소 데이터만 추출
for data in datas :
    print(data)

#리스트 안에 요소/ 원소 (인덱스, 데이터) 추출
for data in enumerate(datas, start=100) :
     print(data)


x = ['std01', 'std02', 'std03']
y = [100, 200, 300]

for data in enumerate(x):  #이르케하면 튜플 형태로 나옴
    print(data)

myDict = {}
for data in enumerate(x):  #이르케하면 딕셔너리 형태
    myDict[data[1]] = y[data[0]]
print(f'myDict => {myDict}')


x = ['std01', 'std02', 'std03']
y = [100, 200, 300]

myDict2 = {}
for idx, key in enumerate(x): #이르케하면 언패킹st
    # #그러면(0,'std01')이런식으로

    myDict2[key] = y[idx]
#이르케하면 for문 돌릴 필요 없이 가능함

print(f'myDict2 => {myDict2}')

