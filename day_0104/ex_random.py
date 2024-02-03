## ----------------------------------------------------------------------
# 모듈(Module) : 특정 목적의 변수, 함수, 클래스를 하나의 파일에 담은 것
# - 예: 수학 관련 변수, 함수, 클래스 => math.py
#       파이썬 기본 제공 변수, 함수, 클래스 => builtin.py
# - 사용법 : import 모듈명
# - 모듈의 기능 사용법 : 모듈명.변수명
#                     모듈명.함수명()
# ----------------------------------------------------------------------
# 사용 하고 싶은 변수, 함수, 클래스가 있는 모듈 포함
import random      # 임의의 수를 추출해주는 변수, 함수, 클래스
import math        # 수학 관련 변수, 함수, 클래스 있는 모듈

# 모듈 안에 있는 변수, 함수, 클래스 사용
print(math.pi)    #이렇게 적어야 math 속 변수 pi 가 나온다.

print(math.factorial(5))

print(random.random())  # random 속 random이라는 함수를 부름

# 0.0 <= ~ < 1.0 사이의 임의의 실수 추출 => random() 함수
for cnt in range(10):
    print(random.random())

# 0.0 <= ~ < 1.0 사이의 임의의 실수 추출 => random() 함수
# 1 <= ~ <= 10 정수를 추출
for cnt in range(10):
    print(int(random.random()*10)+1)

# a<= ~ <=b 사이의 임의의 정수 추출 => randint() 함수
for cnt in range(10):
    print(random.randint(1, 10), end=' ')

print(f'\n')

mylotto = []
end_point = 6
while True:
    if len(mylotto) == end_point: break        # 한줄이면 옆에 쓰기 ㄱㄴ
    num = random.randint(1, 45)
    if num not in mylotto:                     # 중복 제거 위해 작성
        mylotto.append(random.randint(1, 45))

print(f'my lotto => {mylotto}')


#set은 자동으로 중복 제거
mylotto = set()
end_point = 6
while True:
    if len(mylotto) == end_point: break        # 한줄이면 옆에 쓰기 ㄱㄴ
    num = random.randint(1, 45)
    mylotto.add(num)                     #set이라 알아서 중복이 제거됨

print(f'my lotto => {mylotto}')