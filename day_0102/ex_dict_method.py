# ------------------------------------------------------------------------
# dict 데이터 전용 함수 즉 메서드(Method)
# ------------------------------------------------------------------------
# 빈 dict 타입 변수 생성 ----------------------------------------------------
myDict = {}

# 데이터 추가 => myDict[키] = 데이터
myDict['one'] = 100

# 데이터 추가 => update(키=데이터) 메서드
# 주의!! 키는 str타입만 가능, str타입이지만 '', "" 사용 안함
# myDict.update('two',200) #TypeError: update expected at most 1 argument, got 2 -> 1개만 달라
# myDict.update('two' = 200) #홑따옴표 들어가서 안됨
myDict.update(two = 200, _1 = 1000) #여기서 two가 매개변수라서 홑따옴표 ㄴㄴ, 변수니까 변수이름 숫자로 시작 ㄴㄴ

print(myDict)


# 키만 추출해서 읽어오는 메서드   ==> keys() 메서드 --------------------------------------
keys = myDict.keys()
print(f'myDict의 키들 : {keys}, {type(keys)}')


# 값만 추출해서 읽어오는 메서드   ==> values() 메서드 ------------------------------------
values = myDict.values()
print(f'myDict의 값들: {values}, {type(values)}')

# 키와 값을 추출해서 읽어오는 메서드   ==> items() 메서드 ---------------------------------
# (키, 값)인 튜플형식으로 묶어서 나옴
items = myDict.items()
print(f'myDict의 키와 값 묶음: {items}, {type(items)}') 
#print(f'myDict[0]의 키와 값 묶음: {items[0]}, {type(items[0])}') #불가능, 튜플형태라서ㅇㅇ, 리스트로 형변환해야함

# 원소/요소 단위 접근 위해서는 형변화 필요함!!
items = list(myDict.items())
print(f'myDict[0]의 키와 값 묶음: {items[0]}, {type(items[0])}') #리스트로 형변환해서 가능

#위 3가지는 반드시 기억! 딕셔너리는 인덱스 접근이 불가능해서 저 3가지 자주 사용
#파이선 2점대에서는 리스트로도 나왔으나 3점대부터는 메모리 문제로 view 타입으로 바뀜


# 원소/요소 모두 삭제해주는 메서드 => clear() 메서드 --------------------------------------
myDict.clear() #return값이 none이므로 원본이 수정된다
print(f'myDict : {myDict}, {len(myDict)}')

# 원소/요소 데이터 읽기 메서드 => 변수명[키]   ====> 값, get(키)메서드
# => 키가 존재하지 않으면 none 반환
print(f'myDict.get("one") : {myDict.get("one")}, {myDict["one"]}')
print(f'myDict.get("three") : {myDict.get("three")}') #error 발생
print(f'myDict["three"] : {myDict.get["three"]}') #error 발생

# 원소/요소 데이터 읽기 메서드 => 변수명[키]   ====> 값, get(키)메서드
# => 키가 존재하지 않으면 기본값 반환
print(f'myDict.get("three", 0) : {myDict.get("three", 0)}')
#- 키에 해당하는 값이 없다면 0이라는 기본값으로 설정해서 output함



# -----------------------------------------------------------------------------------
# 멤버 연산자    =>  원소 in 여러개 저장 타입
#              =>  원소 not in 여러개 저장 타입
# - 여러개 저장 타입 : str, list, tuple, dict, set
# - 연산 결과 => True / False
# -----------------------------------------------------------------------------------
aList = [1,2,3]
aTuple = (1,2,3)
aDict = {1:100, 2:200, 3:300}

#                   => 데이터 즉 값 존재 여부
print(f'1 in alist = {1 in aList}')
print(f'1 in aTuple = {1 in aTuple}')
#                   => 키 존재 여부  (원소 자리에 키가 들어감)
print(f'1 in aDict = {1 in aDict}')
print(f'100 in aDict = {100 in aDict}')   #100이라는 key가 없으므로 False

