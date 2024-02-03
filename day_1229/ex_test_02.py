#----------------------------------------------------------
# [실습1] 임의의 숫자 데이터 7개를 저장한 리스트를 생성
#        리스트에 원소를 하나씩 화면에 출력하세요
#----------------------------------------------------------

list = [11,22,33,44,55,66,77]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])
print(list[6])
print()

#print(list[0], list[1] .... list[6], sep='\n')   => 이 방식으로 해도 됨

#----------------------------------------------------------
# [실습2] 아래 리스트에서 원소를 화면에 한 줄에 한개씩 출력하세요.
#----------------------------------------------------------

list = [[10,20], [40,50], [70,80,90]]
print(list[0][0])
print(list[0][1])

print(list[1][0])
print(list[1][1])

print(list[2][0])
print(list[2][1])
print(list[2][2])
print()

#----------------------------------------------------------
# [실습3] 좋아하는 계절과 월(month)를 입력 받은 후 각각 변수에 저장
#        변수명은 season, month이다.
#        input은 한번만 사용하도록 한다.
#----------------------------------------------------------
#방법1 = 출제자의 의도
data = input('좋아하는 계절과 월 입력 (예:겨울, 12): ')
list = data.split(',')
season = list[0]
month = list[1]
print(f'좋아하는 계절은 {season}이고 좋아하는 월은 {month}월이다')

#방법2
season, month = input('좋아하는 계절은? '), input('좋아하는 월은? ')
print(f'좋아하는 계절은 {season}이고 좋아하는 월은 {month}월이다')
print()

#---------------------------------------------------------
# [실습4] 1~20으로 구성된 정수 리스트를 생성하세요.
# * 3의 배수 인덱스에 해당하는 정수만 출력하세요
# * 3의 배수 인덱스에 해당하는 점수의 합계를 출력하세요.
#---------------------------------------------------------

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(f'3의 배우 인덱스에 해당하는 정수는 {list[3::3]}이다')
#슬라이싱을 한다면 1개만 뺴도 output은 리스트이다

sum = 0
sum = list[3] + list[6] + list[9] + list[12] + list[15] + list[18]
print(f'3의 배수 인덱스에 해당하는 정수의 합계는 {sum}이다')
