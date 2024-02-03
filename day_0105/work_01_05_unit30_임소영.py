# work_01_05_임소영
# UNIT30 함수에서 위치 인수와 키워드 인수 사용하기

# 연습문제 30.6 : 가장 높은 점수를 구하는 함수 만들기

korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*subject):
    return max(subject)

max_score = get_max_score(korean, english, mathematics, science)
print('높은 점수: ', max_score)

max_score = get_max_score(english, science)
print('높은 점수: ', max_score)



# 심사문제 30.7 : 표준입력으로 가장 낮은 점수, 높은 점수와 평균 점수를 구하는 함수 만들기. 평귡점수는 실수로 출력
'''
# ⚠️ 굴러는 간다. 다만 2차로 최대,최소,평균 추출 과정에서 안됨.
#    내 생각에는 해당 키와 값을 삭제하는 문법?을 아직 모르는 듯 ㅇㅇ

def calc():
    # 빈딕셔너리 생성 → 각 과목 점수 입력 후 딕셔너리에 넣음 → print문으로 확인
    subject = {}
    subject['korean'] = int(input('국어 점수 입력: '))
    subject['english'] = int(input('영어 점수 입력: '))
    subject['math'] = int(input('수학 점수 입력: '))
    subject['science'] = int(input('과학 점수 입력: '))
    print(f'{subject}')
    print(f'{subject.values()}')

    # 1차로 최대값, 최소값, 평균 추출 → 딕셔너리에서 1차의 최대값, 최소값 제거
    average = float(sum(list(subject.values()))/4)
    print('최대값은',max(subject.values()),'최소값은',min(subject.values()),'평균은',average)
    x = max(subject.values())
    y = min(subject.values())
    del subject[x]
    del subject[y]

    # 2차로 최대값, 최소값 평균 추출
    print('최대값은',max(subject.values()),'최소값은',min(subject.values()),'평균은',average)

# 함수호출
calc()
'''


# 책에 제시된 부분으로 풀어봄

korean, english, math, science = map(int, input().split()) #int형식으로 각 변수에 저장

def get_score(korean, english, math, science):
    min_score = min(korean, english, math, science)
    max_score = max(korean, english, math, science)
    return min_score, max_score

def get_average(korean, english, math, science):
    avrg = (korean + english + math + science)/4
    return avrg

min_score, max_score = get_score(korean, english, math, science)
average_score = get_average(korean=korean, english=english, math = math, science = science)

print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))