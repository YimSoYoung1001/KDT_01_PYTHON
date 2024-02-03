# -------------------------------------------------------------
# list의 원소/요소 데이터 변경 및 삭제
# -------------------------------------------------------------
# "Merry Christmas"의 문자 각각 1개를 원소로 가지는 리스트로 생성

# word = "Merry Christmas"
# list = list(word)

msg = list("Merry Christmas")
print(msg)

# => ' ' 데이터를 '***' 변경하기
#string이면 replace하면 됨
print(msg[5])

msg[5] = '***'    #원래 있는 요소를 바꾸려고 변수에 저장함
# string은 이게 안되었지만 list는 되는 이유
# => list는 각 원소는 주소를 가지고 있기 때문에 바꾸는거 가능한
# => string은 하나가 덩어리로 묶여있어서 인덱스 수정 불가능
print(msg)

# 삭제 ===> del 데이터 또는 del(데이터) -----------------------------
del msg[5]   #5번 인덱스를 삭제해줘
print(msg)

del msg[5]   #5번인덱스 삭제함. 즉 주소를 삭제함
print(msg)

del msg      #msg리스트 자체를 삭제함
print(msg)

