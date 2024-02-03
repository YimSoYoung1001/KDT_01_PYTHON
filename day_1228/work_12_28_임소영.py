# work_12_28_임소영

print('1번 문제')
email = 'kim1234@naver.com'
print(email[:6])

web = 'http://www.naver.com'
print(web[11:])

name = '홍길동'
print(name[ : ])

alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRr'
print(alphabet[::2])
print(alphabet[1::2])
word = 'ABC1DEF2GHI3JKL4MNO5PQR6STU7VWX8YZ'
print(word[3::4])

Socialnumber = '881120-1068234'
print(f'생년월일 부분 => {Socialnumber[:6]}')
print(f'숫자 부분    => {Socialnumber[7:]}')

print()
print('2번 문제')
number = int(input('정수입력: '))
print(f'10진수: {number}')
print(f'16진수: {hex(number)}')
print(f' 8진수: {oct(number)}')
print(f' 2진수: {bin(number)}')

print()
print('3번 문제')
word1 = input('첫번째 단어를 입력하세요: ')
word2 = input('두번째 단어를 입력하세요: ')
word3 = input('세번째 단어를 입력하세요: ')

print(f'코드 값이 가장 큰 단어:  {max(word1, word2, word3)}')
print(f'코드 값이 가장 작은 단어: {min(word1, word2, word3)}')

print()
print('4번 문제')
sentence = '오늘은 행복한 목요일입니다.'
in_word = input('단어 입력: ')
print(f'\'{in_word}\' 단어 메시지 존재여부: {in_word in sentence}')
in_word = input('단어 입력: ')
print(f'\'{in_word}\' 단어 메시지 존재여부: {in_word in sentence}')

print()
print('5번 문제')
value = input('단어 입력: ')
code1 = bin(ord(value[0]))
code2 = bin(ord(value[1]))
code3 = bin(ord(value[2]))

code1 = code1[2:]
code2 = code2[2:]
code3 = code3[2:]
print(f"'{value}' 코드값 : {code1}  {code2}  {code3}")


