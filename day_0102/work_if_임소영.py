# 13장 ~ 14장 work_if_임소영

# 13장 ==================================================================
# 연습문제 13.6
x = 5
if x != 10:
    print('ok')

# 심사문제 13.7
price = int(input())
discount = input()

if discount == 'Cash3000':
    print(price - 3000)
else:
    print(price - 5000)


# 14장 ===================================================================
# 연습문제 14.6
score = 75
test = True

if score >= 80 and test == True :
    print('합격')
else :
    print('불합격')

# 심사문제 14.7
scores = input('').split()
score1 = int(scores[0])
score2 = int(scores[1])
score3 = int(scores[2])
score4 = int(scores[3])

if score1 > 100 or score1 < 0 :
    print('잘못된 점수')
else:
    average = (score1 + score2 + score3 + score4)/4

if score2 > 100 or score2 < 0 :
    print('잘못된 점수')
else:
    average = (score1 + score2 + score3 + score4)/4

if score3 > 100 or score3 < 0 :
    print('잘못된 점수')
else:
    average = (score1 + score2 + score3 + score4)/4

if score4 > 100 or score4 < 0 :
    print('잘못된 점수')
else:
    average = (score1 + score2 + score3 + score4)/4

if average >= 80:
        print('합격')
else :
        print('불합격')


