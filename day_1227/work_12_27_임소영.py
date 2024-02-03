#work_12_27_임소영

print('1번 문제')
city = '대구'
bloodtype = 'A'
season = 'winter'
height = '160cm'
phone = '010-5331-4951'
nation = 'korea'

print('==============')
print()

print('2번 문제')
mbti='INFP'
blood='A'
gender='M'
height=171.7
weight=77

print('1번')
print('mbti : INFP', '혈액형 : A', '성별 : M')
print('몸무게 : 77', ' 키 : 171.7')

print('2번')
print('mbti : %s  혈액형 : %s  성별 : %s' %(mbti, blood, gender))
print('몸무게 : %.0f  키 : %.1f' %(weight, height))

print('3번')
print(f'mbti : {mbti}  혈액형 : {blood}  성별 : {gender} \n몸무게 : {weight}   키 : {height}')

print('==============')
print()

print('3번 문제')
print('#1')
print(f'데이터 50 => {type(50)} 타입')
print(f'데이터 0.91 => {type(0.91)} 타입')
print(f'데이터 winter => {type("winter")} 타입')
print(f'데이터 False => {type(False)} 타입')

print('#2')
season = input('좋아하는 계절은? ')
print(f'당신은 {season}을 좋아하는 군요!')
english = input('봄은 영어로? ')
print(f'봄은 {english}입니다.')

print('==============')
print()

print('4번 문제')
print('힙')
print('스택')

print('==============')
print()

print('5번 문제')
print('#1: integer,  float,  string,  bool')
print('#2: 2진수,  8진수,  16진수')

print('==============')
print()

print('6번 문제')
x = int(input('정육면체 가로길이(cm): '))
y = int(input('정육면체 세로길이(cm): '))
z = int(input('정육면체 높이길이(cm): '))

print(f'직사각형 넓이: {x*y}')
print(f'직사각형 부피: {x*y*z}')
