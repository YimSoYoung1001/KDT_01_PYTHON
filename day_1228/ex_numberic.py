'''
논리연산자 => and, or, not
- 결과: True, False
- 동작방식
    * and => A and B : A, B 모두 True일 떄만 True
    * or => A or B : A, B 중 하나 이상 True가 되면 True
    * not => not A : 현재 A의 상태를 반대로 => not True -> False, not False -> True : 토글(toggle)
'''
no1 = 10
no2 = 3
no1, no2 = 10, 3

# and 연산자  ----------------------------------------------------------
# no1은 no2보다 크고 그리고 100보다 큰 수
print( no1 > no2 , no1 > 100)   #서로 따로인 상태
print( no1 > no2 and no1 > 100) #논리연산자로 묶인 조건
print( no1 > no2 and no1 > 100 and no1 > 0)

# or 연산자  ----------------------------------------------------------
# 1개 이상만 True가 되면 True로 결정
no1 = 10
no2 = 3
print( no1 > no2 , no1 > 100)   #서로 따로인 상태
print( no1 > no2 or no1 > 100) #논리연산자로 묶인 조건
print( no1 > no2 or no1 > 100 or no1 > 0)

# or 연산자  ----------------------------------------------------------
# 현재 값을 반대로 즉, True => False, False => True
# False => 0 , True => 1 / 0이 아닌 모든 숫자
print(not False, not True)
print(not 0, not 1)    # 0은 False니까
print(not 2, not -3, not 0.0)   # True => 1 / 0이 아닌 모든 숫자
                    # ㄴ 자동형변환되어서 0.0은 False
                    

'''
객체 비교 연산자 => is, is not
- 결과: True, False
- 동작 방식
    * is => A is B : A, B가 동일한 데이터 타입의 객체 여부
    * is not => A is not B : A, B가 서로 다른 데이터 타입의 객체 여부
'''

print(f'10 is 10 => {10 is 10}') #a가 b의 객체이냐?
print(f'10 is 10.0 => {10 is 10.0}, 10 == 10.0  => {10 == 10.0}') #타입과 내용(?) 비교냐? 값 비교냐?
print(10 is 20)
