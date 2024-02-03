# -----------------------------------------------------------
# filter(함수명, 반복가능 객체)
# - 조건에 맞는 데이터만 반환
# -----------------------------------------------------------
import random                       # random.py 파일의 모든 변수, 함수, 클래스 가져오기
from random import randint, random  # random.py 파일에서 randint와 random 함수만 가져오기
from functools import reduce

# 예) 5 초과 10 미만 데이터만 추출
a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]

def check(data):
    return data > 5 and data < 10    # return값은 T/F

a = list(filter(check, a))   # 여기서 True인 요소만 뽑아줌
# check 함수를 람다로 한다면,, lambda data: data > 5 and data < 10)(a)
print(a)

def f(x,y):
    return x + y
print(reduce(f,a))


# 19~21번 라인을 람다로 정리한다면,,
print(reduce(lambda x, y: x+y, a))

