# --------------------------------------------------------------------
# str 데이터 타입 전용의 함수 즉 메서드 (method) 살펴보기
# - 메서드 (Method)
# - 특정 데이터 타입에서만 사용 가능함 함수를 의미
#     ~ 전용의 함수를 메서드라고 한다. (int 전용의 함수, float 전용의 함수 ~ ..)
# - 사용방법
#   변수명.메서드명()   => msg = 'Good'     msg.메서드명()
#   데이터.메서드명()   => "Good".메서드명()
# --------------------------------------------------------------------
# str을 대문자로 변환 ==> upper() 메서드
print("Good".upper())   # => 이렇게 하면 다 대문자로 바뀜
# 그게 아니라면 각 글자마다 인덱스로 접근해서 각각 하나씩 바꿔야함
# .upper()   =>     #에러뜸. 이거는 내장함수가 아니다. 그래서 문자열뒤에 붙여야 함

# str을 소문자로 변환 ==> lower() 메서드
print("Good".lower())

# str이 모두 대문자인지 검사 후 결과 반환 => isupper() 메서드
print("Good".isupper())

# str이 모두 소문자인지 검사 후 결과 반환 => islower() 메서드
print("Good".islower())

# str이 0~9로 구성되어 있는지 검사 후 결과 반환 => isdecimal() 메서드
print("Good".isdecimal(), "012".isdecimal(), "-9".isdecimal())

# str이 문자로만 구성되어 있는지 검사 후 결과 반환 => isalpha() 메서드
print("Good".isalpha(), "Good2024".isalpha(), "한글".isalpha())
# 한글도 문자로 인식함

# str이 문자, 숫자로만 구성되어 있는지 검사 후 결과 반환 => isalnum()
print("Good".isalnum(), "Good2024".isalnum(), "한글".isalnum())

# str 문자에서 특정 문자/문자열로 시작하는지 검사 후 결과 반환
# 시작 => ??
print("??Happy New".startswith("??"))
print("??Happy New".startswith("!"))

# str 문자에서 특정 문자/문자열로 끝나는지 검사 후 결과 반환
print("flower.jpg".endswith("jpg"))
print("flower.png".endswith("jpg"))
print("flower.png".endswith(("jpg","png","txt")))
# 만약 이 메소드를 몰라도 슬라이싱해서 할수도 있음. or 연산자 나 in 연산자 해서 ㅇㅇ

# str 특정 인덱스 문자를 변경해주는 메서드 => replace() 메서드  --------------
name = "HongGulDong"  # u를 i로 변경하고자 함
print(name[5])

num = 10
num = 'Apple'
#name[5] = 'i' #인덱싱의 방식은 지원하지 않음 ==> 메서드 제공
print(name.replace('u', 'i'))
print(name.replace('o', '*'))  #count 기본값은 해당되는 글자 모두 바꿈
print(name.replace('o', '*',1))


