# work_12_29_book

# UNIT10
#연습문제 10.4
a = list(range(5,-10,-2))
print(a)

#심사문제 10.5
num = int(input('숫자를 입력: '))
b = tuple(range(-10, 10, num))
print(b)

# UNIT11
# 연습문제 11.6
year = [2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
population = [10249679, 10195318, 10143645, 10103233, 10022181, 9930616, 9857426, 9838892]
print(year[-3:])
print(population[-3:])

# 연습문제 11.7
n = -32, 75, 97, -10, 9, 32, 4, -15, 0, 76, 14, 2
print(n[1::2])

# 심사문제 11.8
value = input('입력할 모든 정보를 spacebar로 구분하여 입력: ').split()
value = value[:-5:]
print(tuple(value))

# 심사문제 11.9
word1 = input()
word2 = input()
print(word1[1::2],word2[::2],sep='')
