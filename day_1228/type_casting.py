"""
타입 캐스팅 (type casting)
- 정수 -> 실수, 실수 -> 정수, 정수 -> 논리 등등 다른 데이터 타입으로 변환하는 것
- 함수
  => 정수로 형변환해주는 함수 int()
  => 실수로 형변환해주는 함수 float()
  => 문자열 형변환해주는 함수 str()
  => 논리 형변환해주는 함수 bool()
"""
# int 데이터 타입으로 형변환 -------------------------------
# str ---> int : int(데이터)
print(type(int('200'))) #str을 int로 바꾸는 거
#원래는 변수로 저장해서 한 3줄짜리를 1줄로 한거 근데 이거는 그냥 확인용이니까 굳이 변수로 ㄴㄴ
print(type(int('200day')))
#ValueError: invalid literal for int() with base 10: '200day'
#base10 : 문자 '0~9' = 10진수가 허용되는데 그게 아닌게 있다.
print(type(int('200.4'))) #얘도 마찬가지

# float ---> int : 소수점 이하 데이터 손실 발생
print(type(int(200.4)), int(200.7))

# bool ---> int
# => 0(거짓),1(참) => False, True
print(type(int(False)), int(False), type(False))
print(type(int(True)), int(True), type(True))
print(type(int('True')), int('True'), type('True'))  #str이라 error 발생

# float 데이터 타입으로 형변환 -------------------------------
# str ===> float ('0~9, .') 뒤에 .0이 없으면 알아서 붙여줌
print(type(float('3.5')), float('3.5'))
print(type(float('35')), float('35'))
print(type(float('0x123')), type('0x123')) #error 뜸. 따로 함수가 있음
print(type(float('-123')), float('-123'))

# int ===> float
print(type(float(45)), float(45))
print(type(float(-9)), float(-9))

# bool ===> float
print(type(float(False)), float(False))
print(type(float(True)), float(True))



