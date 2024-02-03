# --------------------------------------------------------------
# 컨프리헨션 (comprehension)
# - List Comprehension, Dict Comprehension, Set Comprehension
# - 이렇게 쓰인 방식이 더 자주 쓰인다.
# --------------------------------------------------------------

# [실습1] aList의 원소 값을 제곱한 값을 원소로 가지는 bList 생성하세요.
aList = [1,2,3,4]

# 일반적 for 방식
bList = []
for a in aList:
    bList.append(a**2)

print(f'aList => {aList}')
print(f'bList => {bList}')

# 컴프리헨션 방식
cList = [ a**2 for a in aList ]
# 8~10번라인을 한줄로 적은 list comprehension
print(f'cList => {cList}')

print()


# [실습2] aList의 원소 값 중에서 짝인 데이터만을 제곱한 값을 원소로 가지는 bList 생성하세요.
bList = []
for a in aList:
    if not a%2:        # not False => True
        bList.append(a**2)

print(f'aList => {aList}')
print(f'bList => {bList}')

# 컴프리헨션 방식
cList2 = [ a**2 for a in aList if not a%2 ]
#          ----  -------------  ----------
#           (3)       (1)          (2)
# (1)에서 a를 꺼내서 (2)에서 판단해서 True이면 (3)이 실행된다.
print(f'cList => {cList}')

print()


# [실습3] aList의 원소 값 중에서 짝인 데이터는 제곱하고, 홀수인 데이터는 그대로 저장한 bList 생성하세요.
bList3 = []
for a in aList:
    if not a % 2:        # not False => True
        bList3.append(a**2)
    else:
        bList3.append(a)
print(f'aList => {aList}')
print(f'bList => {bList}')

# 컴프리헨션 방식
cList3 = [ a**2 if not a%2 else a for a in aList  ]
#          ----  ---------  -----  ------------
#           (3-T)   (2)     (3-F)      (1)
print(f'cList3 => {cList3}')


cList4 = {a : a**2   if not a%2    else a   for a in aList }
print(f'cList4 => {cList4}')
#중괄호로 바꾸고 저렇게 설정해주면 딕셔너리 컴프리헨션

