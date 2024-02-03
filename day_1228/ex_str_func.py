# -----------------------------------------------------------------------
# str 데이터 타입과 관련된 내장 함수
# -----------------------------------------------------------------------
# 원소/요소의 갯수를 알려주는 내장함수 => length의 약자 len()
msg = "christmas2023!"

print(f'len(msg) => {len(msg)}개')
#print(f'len(2024) => {len(2024)}')   #숫자니까 문자가 아니다! 그러므로 len 적용못함

# 문자의 코드값을 알려주는 내장 함수 => ord(문자 1개)
# 사람  ====={인코딩}======>  기계 : 긱 믄자를 0과1의 기계어로 바꾸어준다. 그때 각 문자에 대한 코드값이라 함
print(f"ord('a') => {ord('a')}")

#Hello의 코드값 출력하기
codeH = ord('H')
codeE = ord('E')
codeL = ord('L')
codeO = ord('O')

print(f'Hello의 코드값 => {codeH}{codeE}{codeL}{codeL}{codeO}')
print(f'Hello의 코드값 => {bin(codeH)}{bin(codeE)}{bin(codeL)}{bin(codeL)}{bin(codeO)}')
print(f'Hello의 코드값 => {bin(codeH)[2:]} {bin(codeE)[2:]} {bin(codeL)[2:]} {bin(codeL)[2:]} {bin(codeO)[2:]}')


# 코드값에 해당하는 문자로 반환해주는 내장 함수 => chr(문자 1개)
# 디코딩 (decoding)
# 코드값 65에 해당하는 문자 반환
print(f'chr(65) -> {chr(65)}')

