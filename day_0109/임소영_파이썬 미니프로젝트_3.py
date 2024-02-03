# =====================================================
# 함수 기능: 기분을 기록하기 위해 설문조사해서 점수 계산하기
# 함수 이름: newMood
# 매개 변수: 없음
# 함수 결과: 점수 결과 및 해결책 보여주기
# =====================================================
def newMood():
    # 설문지에 이용자가 자신의 답 입력하기
    print('🟢 모든 질문에는 0~5점 사이로 입력하기')
    print('🟢 0은 전혀아니다. 5는 매우그렇다 \n')

    h1 = 'Q1. 오늘 하루 크게 박장대소 했나요?::️ '
    q_happy(h1)
    h2 = 'Q2. 오늘 당신을 기분 좋게 하는 것을 느꼈나요?: '
    q_happy(h2)
    h3 = 'Q3. 내일도 오늘과 같은 하루가 되었으면 하나요?: '
    q_happy(h3)
    print()

    a1 = 'Q4. 오늘 인상을 찌푸린 적이 있나요?: '
    q_angry(a1)
    a2 = 'Q5. 당신을 화나게 만든 무언가가 곁에 얼마나 있나요?: '
    q_angry(a2)
    a3 = 'Q6. 오늘 하루가 생각대로 흐르지 않는 것이 나를 힘들게 하나요?: '
    q_angry(a3)
    print()

    d1 = 'Q7. 오늘 하루 대부분의 기분이 공허한가요?: '
    q_depressed(d1)
    d2 = 'Q8. 오늘 하루가 아무 의미없다고 느껴지나요?: '
    q_depressed(d2)
    d3 = 'Q9. 내일도 오늘과 같은 하루가 되기 싫은가요?: '
    q_depressed(d2)
    print('\n')

    print('❕오늘의 감정 기록은 끝났습니다 :)')
    print()

    # 주관식으로 이용자가 자신의 짧은 일기 적기
    more = input('❔오늘 하루 있었던 일을 적어볼까요? Y/N 중 하나 입력: ')
    if more in ['Y', 'y']:
        write()
        print()
    elif more in ["N", 'n']:
        print('❕오늘의 일기 기록은 종료합니다 :)')
        print()
    else:
        print('⚠️재입력하세요.')
        more = input('오늘 하루 있었던 일을 적어볼까요? \n Y/N 중 하나 입력: ')
        # 이걸 반복할 수 있을까???????????????

    # 설문조사 점수 계산하기


    # 계산된 점수를 이용해서 기준치와 비교하기
    if happy >= 8 and angry < 8 and depressed < 8 :
        print('당신은 오늘 행복하군요 😉')
        print()

    else :
        print('❔당신의 기분을 개선시킬만한 게 있을까요?')
        print('❔없다면 조금 추천해드릴까요?')
        curious = input('Y/N로 대답하세요: ')

        if curious in ['Y','y']:
            happything()
        elif curious in ['N', 'n']:
            print('그럼 오늘의 기록은 종료됩니다. :)')
            print('\n')
        else:
            pass

# =====================================================
# 함수 기능: 질문지에 사용자의 답변 넣기1
# 함수 이름: q_happy
# 매개 변수: q
# 함수 결과: 0~5 범위의 정수 출력
# =====================================================
def q_happy(q):

    while True:
        qAnswer = input(q)
        if qAnswer.isdecimal():

            q = int(qAnswer)

            if 0 <= q <= 5:
                global happy
                happy += q
                return happy

            else:
                print('⚠️답은 0~5 사이의 정수에서 입력하세요.\n')
        else:
            print('⚠️정수를 입력하세요.\n')
            q_happy(q)


# =====================================================
# 함수 기능: 질문지에 사용자의 답변 넣기2
# 함수 이름: q_angry
# 매개 변수: q
# 함수 결과: 0~5 범위의 정수 출력
# =====================================================
def q_angry(q):

    while True:
        qAnswer = input(q)
        if qAnswer.isdecimal():

            q = int(qAnswer)

            if 0 <= q <= 5:
                global angry
                angry += q
                return angry

            else:
                print('⚠️답은 0~5 사이의 정수에서 입력하세요.\n')
        else:
            print('⚠️정수를 입력하세요.\n')
            q_angry(q)


# =====================================================
# 함수 기능: 질문지에 사용자의 답변 넣기3
# 함수 이름: q_depressed
# 매개 변수: q
# 함수 결과: 0~5 범위의 정수 출력
# =====================================================
def q_depressed(q):
    while True:
        qAnswer = input(q)
        if qAnswer.isdecimal():

            q = int(qAnswer)

            if 0 <= q <= 5:
                global depressed
                depressed += q
                return depressed

            else:
                print('⚠️답은 0~5 사이의 정수에서 입력하세요.\n')
        else:
            print('⚠️정수를 입력하세요.\n')
            q_depressed(q)


# =====================================================
# 함수 기능: 짧은 일기 써서 저장하기
# 함수 이름: write
# 매개 변수: 없음
# 함수 결과: 없음
# =====================================================
def write():
    print('❕입력된 내용은 저장소에 보관됩니다.')
    diary = input('오늘의 나는 무슨 일이 있었을까?\n === 입력하기 ===\n')
    diaryList.append(diary)
    print()


# =====================================================
# 함수 기능: 해결책 제시하기1
# 함수 이름: happything
# 매개 변수: 없음
# 함수 결과: 데이터 print
# =====================================================

def happything():
    start = '이런것들 해보면 어떨까요? 😇'
    one1 = '1️⃣ 같이 이야기 해요. \n  >> https://pushoong.com/ask/2224895407 << \n 위 페이지를 방문하여 같이 감정을 공유해요! '
    one2 = '익명으로 자신의 이야기를 해볼 수 있어요 :)\n'
    two1 = '2️⃣ 심호흡 해요. \n 478 호흡법 \n  - (1) 복식호흡으로 4초간 코로 숨을 들이마쉰다.\n  - (2)  ️7초간 숨을 참으며 멈춘다. '
    two2 = '  - (3)  ️8초간 숨을 내뱉는다. \n  - (4)  ️위 과정을 반복한다.\n'
    three1 = '3️⃣ 감정일기를 적는다. \n 감정일기를 쓰면 어떤 점이 좋을까? \n + 감정에 이름을 붙여보며 막연했던 감정들이 조금 더 분명해지며 해소감이 든다.'
    three2 = ' + 감정에 무작정 휩쓸리지 않고 끊어내어 감정에서 빠져나올 수 있다.\n + 부정적인 감정이 강하게 올라오는 특정 문제에 대해 알아차리고 해결책을 세울 수 있다.'

    print(start)
    print()
    print(one1)
    print(one2)
    print(two1)
    print(two2)
    print(three1)
    print(three2)
    print()

# =====================================================
# 함수 기능: 저장된 시퀀스에서 데이터 꺼내오기
# 함수 이름: lookMood
# 매개 변수: 없음
# 함수 결과: 데이터 print
# =====================================================
def lookMood():
    print('당신의 기록을 볼까요?')
    diaryNum = int(input('당신의 몇 개의 기록을 보고싶나요?: '))
    if diaryNum > len(diaryList):
        print('⚠️조금 더 작은 수를 입력해주세요!')
    else:
        for i in diaryList[-diaryNum:]:
            print('📜')
            print(i)
    print()

# ----------------------------------------------------------------




begin = True
diaryList = []
happy = 0
angry = 0
depressed = 0

while begin:
    for repeat in range(1):
        print()
        print('       ================== ')
        print('     >> 당신의 오늘 기분은? <<')
        print('       ================== ')

        print('   M E N U  ')
        print(' 1. 오늘의 기분을 기록하기')
        print(' 2. 짧은 일기 작성하기')
        print(' 3. 지난 날의 기분 보기')
        print(' 4. 종료 \n')
        user = input('+++ 사용할 메뉴의 번호를 입력하세요: ')
        print()

        if user.isdecimal():
            if user == '1' :
                newMood()

            elif user == '2' :
                write()

            elif user == '3' :
                lookMood()

            elif user == '4' :
                print()
                ending = '''
  ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿          
／                             ＼            
   오늘 당신의 기분은 돌아보았나요?
      그럼 내일 뵙겠습니다 :)
＼＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿／
    　　ｏ
    　　 。
    　　　｡
    　　∧＿∧
    　 (*　･ω･)
    ＿(__つ/￣￣￣/_
    　　＼/　　　/

            '''
                print(ending)
                begin = False
            else :
                print('⚠️메뉴 속 번호를 입력하세요\n\n\n')

        else:
            print('⚠️숫자를 입력하세요.\n\n\n')


    print('❔메뉴를 다시 보시겠습니까?')
    menu_again = input('Y 또는 N으로 입력하세요: ')

    if menu_again in ['Y', 'y']:
        print('메뉴로 돌아갑니다!')
    elif menu_again in ['N', 'n']:
        print()
        ending = '''
  ＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿          
／                             ＼            
   오늘 당신의 기분은 돌아보았나요?
      그럼 내일 뵙겠습니다 :)
＼＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿／
    　　ｏ
    　　 。
    　　　｡
    　　∧＿∧
    　 (*　･ω･)
    ＿(__つ/￣￣￣/_
    　　＼/　　　/

            '''
        print(ending)
        begin = False