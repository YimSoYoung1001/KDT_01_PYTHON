# ----------------------------------------------------
# 지역변수 & 전역변수
# ----------------------------------------------------

def foo():
    #global x        # 전역변수 X
    x = 20           # 전역변수 X에 값 변경
    print(x)         # 전역변수 X
    print(locals())  # 이르케하면 지역범위내의 변수만 나옴

# 전역변수 -----------------------------------------
x = 10

# 함수 호출 ---------------------------------------
foo()
print(x)
print(locals())