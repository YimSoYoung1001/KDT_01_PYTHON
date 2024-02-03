# 키워드 인수

def personal_info(name, age, address):
    print('이름: ', name)
    print('나이: ', age)
    print('주소: ', address)

#personal_info('홍홍홍', 30, '용산동')

x = {'name':'김이름', 'age':30, 'address':'용산동'}
personal_info(*x)
print('='*30)
personal_info(**x)


print()
print('------------------------------------------------------------------------')



# 키워드 인수 + 가변 인수

def info(**kwargs):                           #가변인수로 여러개가 들어갈수있다.
    print(kwargs)
    for kw, arg in kwargs.items():
        print(f"{kw}:{arg}")


y = {'name':'가나다라마바사'}
info(**y)                                    #키워드인수이다.
print('='*30)

y = {'name':'홍길동', 'age':20, 'address':'한남동'}
info(**y)
