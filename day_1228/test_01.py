print('[실습1] 2개 숫자 데이터 입력 받은 후 2개의 값을 산술연산결과 출력')
x = int(input('첫번쨰 숫자를 입력하세요: '))
y = int(input('두번째 숫자를 입력하세요: '))

print(f' {x} + {y} = {x+y}')
print(f' {x} - {y} = {x-y}')
print(f' {x} * {y} = {x*y}')
print(f' {x} / {y} = {x/y}')    ##여기서 소수점을 제한하려면 어케 해야함? .1f (소수점이하에서~)
print(f' {x} // {y} = {x//y}')
print(f' {x} % {y} = {x%y}')
print(f' {x} ** {y} = {x**y}')

print()

print('[실습2] [실습1]에서 입력받은 숫자 데이터를 활용하여 비교연산결과 출력')
print(f' {x} > {y}  => {x>y}')
print(f' {x} < {y}  => {x<y}')
print(f' {x} >= {y} => {x>=y}')
print(f' {x} <= {y} => {x<=y}')
print(f' {x} == {y} => {x==y}')
print(f' {x} != {y} => {x!=y}')

print()

print('[실습3] [실습1]에서 입력받은 숫자 데이터 활용하여 최대값과 최소값을 추가로 입력받은 후 논리연산 결과 출력')
Max = int(input('임의의 최대값을 입력하세요: '))
Min = int(input('임의의 최소값을 입력하세요: '))

print(f' {x} > {y} and 10 > {Max}  => {x > y and 10 > Max}')
print(f' {x} > {y} and 10 > {Min}  => {x > y and 10 > Min}')
print(f' not 10       => {not 10}')       #그냥 확인하려고 냄

print(f'not {x} => {not x}')
print(f'not {y} => {not y}')
# not 연산자 => not 데이터 / 변수명 / 연산식
