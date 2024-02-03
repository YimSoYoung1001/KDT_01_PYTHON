# --------------------------------------------------------------------------
#  함수와 클래스
# --------------------------------------------------------------------------

# 변수에 어떤 데이터를 저장하고 있는지 확인 함수 => type(변수명)
data = 1
print(f'data Type => {type(data)}')

data = 'Good'
print(f'data Type => {type(data)}')

# 함수명의 타입
print(f'id() Type => {type(id)}')

# 사용자 정의 함수 ----------------------------------------------
# 함수 기능 : 2개 정수 더한 후 결과 출력 기능
# 함수 이름 : addTwo
# 매개 변수 : n1, n2
# 함수 결과 : 없음  (바로 print해달라 했으니까)
# ------------------------------------------------------------

def addTwo(n1, n2):
    print(n1+n2)

# 함수의 타입 출력 ===> type() 내장 함수 사용 => class function
print(type(addTwo))
# 함수도 클래스 안에 하나의 객체가 된다.
# 변수와 함수명을 부르면 그 주소로 가서 시작해준다.


# ---------------------------------------------------------------------------------
# 함수와 변수
# - 함수명은 코드의 시작주소를 저장하고 있음
# - 함수명을 변수에 대입가능
# ---------------------------------------------------------------------------------
test = addTwo  #함수명을 대입함 #함수도 객체라서 변수에 저장가능
#만약 저기서 호출한거를 대입하면 그 결과값을 대입한거임! 다르다

print(f'test => {id(test)}, {type(test)}')
print(f'addTwo => {id(addTwo)}, {type(addTwo)}')
#둘은 같은 주소를 가지고 있음을 알수있다.

test(10, 20)
addTwo(10, 20)


# --------------------------------------------------------------------
# [활용 예]
# - 1 ~ 10 범위에서 임의의 정수 5개를 저장
# - 중복된 점수 저장 가능
# --------------------------------------------------------------------
import random

# 내가 한 방식
x1 = random.randint(1,10)
x2 = random.randint(1,10)
x3 = random.randint(1,10)
x4 = random.randint(1,10)
x5 = random.randint(1,10)
print(x1, x2, x3, x4, x5)

# 강사님 방식
nums = []

for count in range(5):
    nums.append(random.randint(1,10))

# 5개의 정수에서 최대값, 최소값, 내림차순 정렬된 값, 합계, 개수 출력
print(f'최대값 : {max(nums)}')
print(f'최소값 : {min(nums)}')
print(f'내림차순 정렬 : {sorted(nums, reverse = True)}')
print(f'합계 : {sum(nums)}')
print(f'개수 : {len(nums)}')

# 여러개의 함수이름을 변수에 저장 => 리스트 사용함
funs = [max, min, sorted, sum, len]

for f in funs:
    if f == sorted:
        print(f(nums, reverse = True))
    else:
        print(f(nums)) #함수 원소를 빼와서 호출시켜서 작동시킴

# 딕셔너리 형태로 출력까지 되도록 해본다 ------------------------------------------
# 내 방식
funsDict = {}

funsDict['최대값'] = max(nums)
funsDict['최소값'] = min(nums)
funsDict['내림차순 정렬'] = sorted(nums, reverse = True)
funsDict['합계'] = sum(nums)
funsDict['개수'] = len(nums)

print(funsDict)
# for key, value in funsDict:
#     print(f'{key} : {value(nums)}')

# 강사님 방식
funDict = {'최대값':max, '최소값':min, '정 렬':sorted, '합 계':sum, '갯 수':len}
for k, v in funDict.items():
    if k == '정 렬':
        print(f'{k} : {v(nums, reverse = True)}')
    else:
        print(f'{k} : {v(nums)}')


