# ========================================
# Unit 5
# ========================================

# 연습문제 5.5
distance = int(input('당신이 거주하는 아파트와 도로와의 거리는? '))
noise = 0.2467 * distance + 4.159
print(noise)   #연산결과 값
print(f'당신의 아파트에서 가장 소음이 심한 층수는 {int(noise)}층입니다.')

#심사 문제 5.6
AP = 102     # AP = Ability Power, 주문력
kill = AP * 0.6 + 225
print(f'당신의 캐릭터의 AP가 {AP}일 때 왜곡의 스킬을 당하면 {kill}만큼의 피해를 받습니다.')


# ========================================
# Unit 6
# ========================================

# 심사문제 6.7
a = 50
b = 100
c = 'None'
print(a)
print(b)
print(c)

# 심사문제 6.8
korean = int(input('국어 점수를 입력하세요: '))
english = int(input('영어 점수를 입력하세요: '))
math = int(input('수학 점수를 입력하세요: '))
science = int(input('과학 점수를 입력하세요: '))
average = (korean+english+math+science)/4
print('당신의 평균은 %.0f'%average)


