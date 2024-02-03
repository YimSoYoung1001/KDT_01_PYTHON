# -----------------------------------------------------------------------------
# 다양한 dict 자료형   =>  key:value   : 이게 한개의 데이터 덩어리
# - key로 데이터를 찾기/읽기/삭제/변경
# - key 중복X  => 마지막 데이터가 key의 값으로 저장
# -----------------------------------------------------------------------------
# 이름, 점수 저장하기
jumsuDict = {'Hong':100, 'Park':98, 'Kim':88, 'Hong':50, 'Hong':77}

# 'Hong'키가 여러번 저장되면 제일 마지막 데이터가 저장됨!
print(f'jumsuDict => {len(jumsuDict)}개, {jumsuDict}')

# 이름/학년을 키로 해서 점수를 저장하기 ----------------------------------------------
jumsuDict = {('Hong',1):100, ('Park',3):98, ('Kim',1):88, ('Hong',4):50, ('Hong',2):77 }
# - list는 변경이 되는거라 에러뜸, 그러므로 튜플로 묶어야함
# - key는 리스트가 안되지만 값은 리스트가 가능함
# - 이때는 ['Hong',1] 이 덩어리가 키가 된다.
print(f'jumsuDict => {len(jumsuDict)}개, {jumsuDict}')
print(f"jumsuDict[('Hong',2)] => {jumsuDict[('Hong',2)]}")
print(f"jumsuDict[('Hong',1)] => {jumsuDict[('Hong',1)]}")
                                #중괄호 대괄호 구분해!!!!!!!!!!!!!!!!!!!

# 키의 데이터 타입 동일해야 하나요?  => 아닙니다.
testDict = {1:'Hong', 2.0:'Kim', False:100, "name":'HongGilDong'}
print(f'testDict => {len(testDict)}개, {testDict}')


# 빈 딕셔너리 생성
emDict = {}
print(f'emDict => {type(emDict)}, {len(emDict)}개')

#빈리스트, 빈튜플, 빈딕셔너리 => bool 하면 False