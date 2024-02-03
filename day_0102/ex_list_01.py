#---------------------------------------------------------------------
# list => 여러개의 데이터를 저장하는 데이터 타입
# - 문법 => [데이터1, 데이터2, ,,,, , 데이터n]
# - 원소/요소 => 식별하기 위해서 인덱스(index) : 파이썬에서 명명해줌
# - 인덱싱 기능 / 슬라이싱 기능 모두 사용 가능
#---------------------------------------------------------------------
# 1~50 범위의 7의 배수에 해당하는 점수로 구성된 리스트 생성
sevens = range(7,51,7) #7의 배수는 7부터 시작이니까 start = 7로 설정해야함
# => range ==> list 형변환
sevens = list(sevens)
# sevens = list(range(7,51,7))  이렇게 한 줄도 가능


# str 데이터 타입 => 인덱싱 ----->  요소 변경 X
# 리스트가 변경이 가능했던 이유는 리스트 속 각 data는 주소를 가지고 있었기 때문
# 제일 첫번째 인덱스에 있는 원소를 삭제
# ==> del 삭제하고 싶은 데이터  또는 del(삭제하고 싶은 데이터)    소괄호는 써도되고 안써도되고
del sevens[0] #7삭제
del sevens[0] #14삭제 (처음에 [1]이었던게 [0]이 되어 걔가 삭제)
#del sevens    #리스트 객체 주소를 저장하는 변수를 삭제 (리스트 전체 사라짐)


# -----------------------------------------------------------------------
# str 데이터 타입 => 인덱싱 -----------> 요소 추가 X
# 리스트에 인덱싱 방식으로 원소/요소 데이터 변경/삭제 가능
# 리스트에 인덱싱 방식으로 원소/요소 데이터 추가 불가능
# -----------------------------------------------------------------------
# 요소 갯수 5개 => 0 ~ 4
#sevens[5] = 56  # index out of range 에러 발생
sevens[4] = 56
print(f'sevens => {sevens}')

