# work_01_05_unit24_임소영

# 연습문제 24.4
# 파일경로에서 파일명만 출력하라
path = 'C:\\Users\\dojang\\AppData\\Local\\Programs\\Python\\Python36-32\\python.exe'
filename = path.split('\\')
filename = filename[-1]
print(filename)



# 심사문제 24.5
# 표준입력으로 문자열이 입력. 'the'의 개수 출력하는 프로그램 인출 ('the'만 ㅇㅇ. 'them','there','their'등은 포함 ㄴㄴ)
# ⚠️ 그냥 바로 count하면 답이 8로 나온다. them their 같은 것들이 포함됨
# ⚠️ 아래와 같이 하면 답이 4가 나옴
sentence = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
sentence = sentence.split()
list = []

for word in sentence:
    word = word.strip(',.')
    if word == 'the':
        list.append(word)

print(len(list))

# sentCount = sentence.count('the') #이렇게 하면 일단 the와 the가 포함된 거 까지 count 됨
# print(sentCount)


# 심사문제 24.6
# 표준입력으로 물품 가격 여러개가 문자열 한줄로 입려되고 각 가격은 ;으로 구분됨
# 높은 가격순으로, 가격의 길이는 9로, 오른쪽으로 정렬, 천단위에 콤마 넣은 뒤 출력
'''
1) 입력된 문자열은 세미콜론으로 split
2) 높은 가격순으로 정렬 
3) 가격의 길이를 9로, 오른쪽으로 정렬
3) 천단위 콤마 적용
4) print
'''

money = '54900;83000;158000;367500;250000;59200;128500;1304000'
money = money.split(';')
money = list(map(int,money))
# 높은 가격순으로 정렬
money.sort(reverse=True)
money = list(map(str,money))
# 요청사항에 따라 문자 수정
for m in money:
    m = int(m)
    m = format(m, ',')
    print(f'{m: >9}')

# for문안에 이렇게 넣으니까 정렬 적용이 안됨
#     m = '{0: >9}'.format(m)      #여기서 무언가 잘못한듯
#     m = int(m)
#     print(format(m, ','))



