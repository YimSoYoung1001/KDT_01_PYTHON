# --------------------------------------------------------
# [질문] 10명의 학생에 대한 학점을 저장하기
# - 학생의 이름과 학점
# --------------------------------------------------------
# 방법1) 학생 이름 변수 5개 => stdName1 ~ stdName5
#       학점 변수 5개     => jumsu1 ~ jumsu5


# 방법2) 학생 이름 변수 5개 => stdNames = [학생이름1, ... , 학생이름5]
#       학점 변수 5개 => stdJumsus = [점수1, ... , 점수5]
stdNums = ['std01', 'std02', 'std03', 'std04', 'std05']
stdJumsus = [90, 80, 100, 70, 60]

# => 학번 03번 학생의 학번과 점수를 출력하세요 ~
idx = stdNums.index('std03')

print(f'{stdNums[idx]}학번 학생의 점수: {stdJumsus[idx]}')


# 방법3) 학생 이름 변수 5개 => stdNames = [학생이름1, ... , 학생이름5]
#       학점 변수 5개 => stdJumsus = [점수1, ... , 점수5]
stdNumsJumsus = [['std01',90], ['std02',80], ['std03',100], ['std04',70], ['std05',60]]
# 이상태에서는 인덱스 찾는게 골치아프다


# -----------------------------------------------------------------------------
# dict 자료형
# - 연관되어 있는 데이터를 하나로 묶어서 저장하는 방식 => 연관배열
# - 형 =>  키 : 데이터         (예 -   주민번호:이름, 학번:전공)
# - 조건 => 키가 중복되면 안됨!
# - 문법 => {키1:데이터1, 키2:데이터2, ... , 키N:데이터N}
# -----------------------------------------------------------------------------
stdNumsJumsu = {'std01':90, 'std02':80, 'std03':60, 'std04':70, 'std05':30}
                # 이거는 원소가 5개이다.

print(f'stdNumsJumsu: {type(stdNumsJumsu)}, {stdNumsJumsu}')
print(f'len(stdNumsJumsu): {len(stdNumsJumsu)}')

# 원소 읽는 방법 => 변수명[키]
print(f" stdNumsJumsu['std03'] => {stdNumsJumsu['std03']}")
# 딕셔녀리는 인덱스 접근이 없다.

# 마지막 원소 지정하는 -1 사용 ==> -1에 대한 키가 없으면 ERROR
# print(f'stdNumsJumsu[-1] => {stdNumsJumsu[-1]}')

# -------------------------------------------------------------------------------
# 원소/요소 추가 방법  => 변수명[새로운 키] = 데이터
# -------------------------------------------------------------------------------
# 학번 10인 학생의 점수 99.8 저장 즉 추가하기
stdNumsJumsu['std10'] = 99.8
print(f'stdNumsJumsu: {type(stdNumsJumsu)}, {stdNumsJumsu}')
print(f'len(stdNumsJumsu): {len(stdNumsJumsu)}')


# -------------------------------------------------------------------------------
# 원소/요소 데이터 변경 => 변수명[기존 키] = 새로운 데이터
# -------------------------------------------------------------------------------
# 학번 10인 학생의 점수 99점으로 변경
stdNumsJumsu['std10'] = 99
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {stdNumsJumsu}')


# -------------------------------------------------------------------------------
# 원소/요소 데이터 삭제 => del 변수명 [키] 또는 del(변수명[키])
# -------------------------------------------------------------------------------
del stdNumsJumsu['std10']
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {stdNumsJumsu}')
del stdNumsJumsu['std02']
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {stdNumsJumsu}')
del stdNumsJumsu['std']
print(f'stdNumsJumsu : {len(stdNumsJumsu)}개, {stdNumsJumsu}')  #key가 없어서 error 발생
#중복된 키를 넣으면 마지막에 설정된 값으로 변경됨

