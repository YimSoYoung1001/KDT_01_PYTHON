# work_01_05_unit25_임소영

# 연습문제 25.7
# 평균 점수 계산
maria = {'korean':94, 'english':91, 'math':89, 'science': 83}
sum = 0

for value in maria.values():
    sum += value
average = sum / 4

print(average)

# 책 예시 답
maria = {'korean':94, 'english':91, 'math':89, 'science': 83}
average = sum(maria.values()) / len(maria)
print(average)


# 심사문제 25.8
# 표준입력으로 문자열 여러개와 숫자 여러개가 두줄로 입력됨. 첫줄은 키 두번쨰 줄은 값으로 해서 생성
# 딕셔너리에서 키가 'delta'인 키-값 쌍과 값이 30인 키-값 쌍을 삭제하는 코드를 완성하라

keys = input().split()
values = input().split()

x = dict(zip(keys, values))

x.pop('delta')

x = {key:value for key, value in x.items() if value != '30'}


print(x)

