# --------------------------------------------------------------------
# str 데이터 타입 전용의 함수 즉 메서드 (method) 살펴보기
# - 메서드 (Method)
# - 특정 데이터 타입에서만 사용 가능함 함수를 의미
#     ~ 전용의 함수를 메서드라고 한다. (int 전용의 함수, float 전용의 함수 ~ ..)
# - 사용방법
#   변수명.메서드명()   => msg = 'Good'     msg.메서드명()
#   데이터.메서드명()   => "Good".메서드명()
# --------------------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => index()
# - 왼쪽 ------> 오른쪽, 제일 먼저 발견되는 문자의 인덱스 반환

data = "Merry Christmas"
#원래는 숫자를 하나하나 헤아려야함
print(f"data.index('C') => {data.index('C')}")
print(f"data.index('r') => {data.index('r')}")
print(f"data.index('r', 4) => {data.index('r', 4)}")
print(f"data.index('r', 3) => {data.index('r', 3)}")
print(f"data.index('r', data.index('r')+1) => {data.index('r', data.index('r')+1)}")

first_r=data.index('r')     #0번원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기
second_r=data.index('r',first_r + 1)   #첫번째 'r'인덱스 이후 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기
third_r=data.index('r',second_r + 1)   #두번째 'r'인덱스 이후 원소부터 하나씩 검사해서 'r'에 해당하는 인덱스 찾기



# ---------------------------------------------------------------------------
# str 데이터에서 특정 문자의 인덱스를 반환하는 메서드 => find()
# - 왼쪽 ====> 오른쪽, 제일 먼저 발견되는 문자의 인덱스 변환
# - 존재하지 않는 str 인덱스 찾을려고 하면 -1 반환
# ---------------------------------------------------------------------------
# !의 인덱스를 찾기
#print(f"data.index('!') => {data.index('!')}")  #notfound error 발생



# --------------------------------------------------------------------------
# str 데이터에서 문자열 분리해주는 메서드 => split() 메서드
# - 기본값 : 스페이스 바, 공백 기준으로 1개의 str을 여러 개의 str 분리
# - 반환값/결과값/리턴값 : 여러 개의 str을 담아서 리스트(List)로 반환
# --------------------------------------------------------------------------
data = "Happy New Year"
print(data.split())

print(type(data.split()))

# str에서 공백을 기준으로 str 나누기
datas=data.split()
print(type(datas), datas)

# list에 저장된 원소/요소 하나씩 읽기 => 변수명[인덱스]
print(f"datas[0]  => {datas[0]}")
print(f"datas[1]  => {datas[1]}")
print(f"datas[-1] => {datas[-1]}")

datas=data.split('-')
# 이렇게 하면 기준에 따라 나눌게 없으니까 리스트에 원소가 1개이다.

juminNo = '123456-1234567'
birth = juminNo[:6]   #이거는 하드코딩이다. 이러면 변화에 대응하지 못해서 bad coding
number = juminNo[7:]
print(birth)
print(number)
print()
birth1 = juminNo[:juminNo.index('-')]
number1 = juminNo[juminNo.index('-')+1:]
print(birth1)
print(number1)

print()
