'''
데이터를 메모리에 저장하는 방법
=> 파이썬 문법 :    변수명 = 저장할 데이터
=> 파이썬의 변수는 '힙 영역에 저장된 데이터 주소'를 저장하는 변수
=> 참조 변수
'''

# 나이를 메모리에 저장하기
# => 나이 : 정수 int ===> 힙 영역
# => 변수 ==> age  100이라는 데이터의 주소값은 age라는 변수에 저장된다. 그래서 '스택에 저장된 주소'를 쉽게 찾을 수 있게 변수로 지정
# 그래서 힙영역에서 그 주소로 찾아가서 "홍길동"을 찾아낸다.
age = 100
# 'age' = 100 <= 이거는 변수가 아니라 데이터로 인식함

# 이름을 메모리에 저장하기
# => 이름: 문자 str ===> 힙 영역
# => 변수: name
_name = '홍길동'
name = "홍길동"
name99 = '홍길동'
# 99name = "홍길동"    <-- 이거는 X , 숫자는 변수 이름으로 첫번째 불가
# my name = "홍길동"   <-- 공백 불가능 공백 대신에 _ (언더바)

#------------------------------------------------------------------------------

# 메모리에 저장은 됨 -> 그러나 저장된 데이터의 위치 (주소)를 알수없음 -> 다시  사용 불가
2024
"good luck"

year = 2024      # 2024 데이터가 저장된 주소를 year 이름이 붙은 메모리 저장
print(year)

# '데이터의 주소'를 확인하는 내장 함수 => id (실제 데이터) / id (변수명)

id(2024) #아이디만 물어봤다. 그런데 우리가 출력을 명령하지 않았으므로 print 를 해야함
print(id(2024))
print(id(year))   #year자리에는 결국 2024가 들어감

year = 2023
print(id(year))

year = '2023'       #문자/글자 str
print(id(year))

# --------------------------------------------------------------------------------------
# 변수가 저장하고 있는 데이터의 종류 즉, 데이터 타입을 알려주는 함수 => type(데이터) 또는 type(변수명)
# --------------------------------------------------------------------------------------

print(type(2024))
print(type(4.))
print(type('4.'))

# 클래스는 레시피와 같다. 레시피만 있다고 해서 요리가 완성되지 않는다.
# 재료가 있는 밀키트가 있어야 요리를 할 수 있다. 이때 밀키트는 '힙 영역에 데이터가 저장된 것'과 유사하다.
# 힙 영역에 클래스 방식대로 데이터가 저장됨  =>  객체 object


