# [실습1] ------------------------------------------------------------
# 좋아하는 정수를 하나 저장한 후 짝수이면 '짝수입니다'
# 홀수면 '홀수입니다'를 출력하라
# -------------------------------------------------------------------

mynum = int(input('좋아하는 정수를 하나 입력하세요: '))

if mynum % 2 == 0:
    print(f'{mynum}은 짝수입니데이')
else :
    print(f'{mynum}은 홀수입니데이')

if mynum % 2 :  #만약에 1이 나오면 이건 True니까
    print(f'{mynum}은 홀수입니데이')
else :
    print(f'{mynum}은 짝수입니데이')



# [실습2] ------------------------------------------------------------
# 좋아하는 정수를 하나 저장한 후 양수이면 '00은 양수입니다'
# 음수면 '00은 음수입니다.'
# 0이면 '00은 영입니다.' 출력하라
# -------------------------------------------------------------------
# 다중 조건문 => 조건문이 2개 이상 되는 경우
mynum = int(input('좋아하는 정수를 하나 입력하세요: '))

if mynum > 0:
    print(f'{mynum}은 양수')
elif mynum == 0:                #다중조건문
    print(f'{mynum}은 영')
else :
    print(f'{mynum}은 음수')

#print("홀수입니다") if int(input("좋아하는 정수 입력 : "))%2 else print("짝수입니다")
#이르케 한줄코딩도 가능하대


# [실습2] ------------------------------------------------------------
# 좋아하는 정수를 하나 저장한 후 양수이면 '00은 양수입니다'
# 음수면 '00은 음수입니다.'
# 0이면 '00은 영입니다.' 출력하라
# -------------------------------------------------------------------
# 중첩 조건문 => 조건문 안에 조건문이 존재하는 경우
mynum = int(input('좋아하는 정수를 하나 입력하세요: '))

if mynum ==0:
    print(f'{mynum}은 영')
else:
    if mynum>0:
        print(f'{mynum}은 양수')
    else:
        print(f'{mynum}은 음수')


