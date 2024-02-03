# 12장 work_dict_임소영
# 연습문제 12.4
camille = {'health':575.6,'health_regen':1.7,'mana':338.8, 'mana_regen':1.63, 'melee': 125, 'attack_damage':60, 'attack_speed': 0.625,'armor': 26, 'magic_resistance': 32.1, 'movement_speed':340}
print(f"게임 캐릭터의 체력(health)는 {camille['health']}")
print(f"게임 캐릭터의 이동속도(movement speed)는 {camille['movement_speed']}")

# 심사문제 12.5
word = input('키와 값을 스페이스바로 구분하여 입력: ').split()
dict = {}
dict[word[0]] = word[1]
print(dict)

word = input('키와 값을 스페이스바로 구분하여 입력: ').split()
dict[word[0]] = word[1]

word = input('키와 값을 스페이스바로 구분하여 입력: ').split()
dict[word[0]] = word[1]

word = input('키와 값을 스페이스바로 구분하여 입력: ').split()
dict[word[0]] = word[1]

word = input('키와 값을 스페이스바로 구분하여 입력: ').split()
dict[word[0]] = word[1]
print(dict)


# ===================== 12.5 강사님 답안 ==============================================
# 문제의 의도는 zip을 쓰란말 같음
# 반복문을 쓰는게 좋긴한데 그게 아니면 아래와 같이 해야함

twodata = input('문자열4~5개, 실수 숫자 4~5개를 두줄로 입력 \n 단, 문자열과 실수 숫자 갯수는 동일 \n (예: aa bb , 3. 5.)      :')

# key와 value로 데이터 분리
datas = twodata.split(',')
keys = datas[0].split()
values = datas[1].split()

'''
keys, values = twodata.split(',')
# 이렇게 하면 34~36번 라인이 한줄로 코딩 가능
'''

# 입력 데이터 존재 여부 체크
if (len(keys) == 4 and len(values) == 4) or (len(keys) == 5 and len(values) == 5):
    print("입력 OK")
    dataDict = {}
    if len(keys) == 4:
        dataDict[keys[0]] = values[0]
        dataDict[keys[1]] = values[1]
        dataDict[keys[2]] = values[2]
        dataDict[keys[3]] = values[3]
        print(dataDict)
    else :
        dataDict[keys[0]] = values[0]
        dataDict[keys[1]] = values[1]
        dataDict[keys[2]] = values[2]
        dataDict[keys[3]] = values[3]
else:
    print('입력데이터 없음')
