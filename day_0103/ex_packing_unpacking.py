# ------------------------------------------------------
# 팩킹(Packing) & 언팩킹(Unpacking)
# ------------------------------------------------------

msg = "Happy New Year"

# 팩킹 (Packing) 방식 -----------------------------------
msgList = msg.split()
print(msgList[0], msgList[-1])

# 언팩킹(Unpacking) 방식 ---------------------------------
# 데이터수와 변수 수가 동일해야함 !!
m1, m2, m3 = msg.split()
print(m1, m2, m3)

# 데이터수와 변수수가 달라서 에러 발생
#m1, m2 = msg.split()
#print(m1, m2)

# 변수를 여러개 생성하는 경우 --------------------------------
age = 12
name = 'Hong'
job = '학생'

# 튜플을 언팩킹으로 생성 가능
info = (12, 'Hong', '학생')
info2 = 12, 'Hong', '학생'
# age1 = info2[0]
# name1 = info2[1]
# job1 = info2[2]

age1, name1, job1 = 12, 'Hong', '학생'
#32번 라인이면 28~30번 라인을 사용하지 않아도 됨
#바로바로 꺼내쓸꺼면 언팩킹 방식으로 튜플을 생성함
#튜플을 꺼내읽을수 있으니까
