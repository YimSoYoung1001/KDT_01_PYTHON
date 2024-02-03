# work_01_05_임소영
# UNIT 22

# 연습문제 22.9 : 리스트를 사용하여 문자열 길이가 5인것만 리스트 형태로 출력
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = list(word for word in a if len(word) == 5 )

print(b)


# 심사문제 22.10 : 2의 거듭제곱 리스트 생성
# 표준 입력으로 정수 2개 입력 (첫숫자는 1~20, 두번쨰숫자는 10~30, 첫번째수 < 2번째수)
# 2의 거듭제곱 리스트를 출력 (지수의 범위는 첫숫자부터 두번째 숫자 까지)
# 최종출력은 리스트의 2번째요소와 뒤에서 2번쨰 요소는 삭제한 뒤 한다.

'''
분해
1) 일단 두개의 값을 2개의 변수로 구분
2) if문으로 입력된 값이 조건에 맞는지 and ㅇㅇ
3) 거듭제곱 리스트 만듬
4) 앞에서2번째, 뒤에서2번째 삭제
5) print()
'''


number = input('2개의 숫자를 스페이스바로 구분하여 입력: ')
# one, two = number.split()
# one = int(one)
# two = int(two)

one, two = list( map(int, number.split()) )

if 1<=one<=20 and 10<=two<=30 and one<two:
    list2=[2**x for x in range(one, two + 1)]
else:
    print('잘못입력함. \n 첫번쨰 숫자는 1~20, 두번째 숫자는 10~30이어야 하고 두번쨰 숫자가 첫번째숫자보다 커야한다.')

del list2[1]
del list2[-2]
print(list2)

