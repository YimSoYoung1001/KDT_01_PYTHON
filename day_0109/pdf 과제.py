# ---------------------------------------------------------------------------
# pdf 과제
# ---------------------------------------------------------------------------



# 3번
def work():
    while True:
        user = input('알파벳 또는 숫자를 입력하세요: ')
        if user.isdecimal():
            user = int(user)
            print('◎'*user)

        elif user.isalpha():
            if user in ['q', 'Q']:
                break
            elif user != 'q' and user.isupper():
                print('♠')
            elif user != 'Q' and user.islower():
                print('♤')


work()