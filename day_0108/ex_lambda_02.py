# 리스트 안에 모든 원소를 더한 합계를 출력
datas = ['1', '4', '9']

for idx, d in enumerate(datas):
    datas[idx] = int(d)

print(datas)

# => 내장함수 map()
datas = list(map(int, datas))
print(datas)

datas = list(map(float, datas))
print(datas)

# => 원소에 *100한 값을 리스트에 저장하기
def multiValue(x):
    return x * 100

datas = list(map(multiValue, datas))
print(datas)

datas = list(map(lambda x:x*100, datas))  # 여기서 x는 datas에서의 원소를 저장하는 매개변수
print(datas)