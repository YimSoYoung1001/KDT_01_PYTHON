# ==============================================
# UNIT 22
# ==============================================

# 연습문제 22-9
a = ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) == 5]
print(b)

# 심사문제 22-10
'''
분해
1) 일단 두개의 값을 2개의 변수로 구분
2) if문으로 입력된 값이 조건에 맞는지 and ㅇㅇ
3) 거듭제곱 리스트 만듬
4) 앞에서2번째, 뒤에서2번째 삭제
5) print()
'''
number = input('2개의 숫자를 스페이스바로 구분하여 입력: ')
one, two = number.split()
one = int(one)
two = int(two)
if 1<=one<=20 and 10<=two<=30 and one<two:
    list2=[2**x for x in range(one, two + 1)]
else:
    print('잘못입력함. \n 첫번쨰 숫자는 1~20, 두번째 숫자는 10~30이어야 하고 두번쨰 숫자가 첫번째숫자보다 커야한다.')

del list2[1]
del list2[-2]
print(list2)