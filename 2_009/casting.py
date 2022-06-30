# 빈 문자 -> false
print('빈 문자(데이터 없음) -> false')
var = ''
print(type(var))

var = bool(var)
print(type(var))
print(var)
print('-------------')

# 공백문자 -> True
print('공백문자(데이터 있음) -> True')
var2 = ' '
print(type(var2))

var2 = bool(var2)
print(type(var2))
print(var2)
print('----------')
# 문자열 -> 논리
# 문자열이 존재하면 논리는 다 Ture!
print('문자열 -> 논리')
a1 = 'True'
a2 = 'False'
print(type(a1))
print(type(a2))

print('----------')

print('문자열이 존재하면 논리는 다 Ture!')
a1 = bool(a1)
a2 = bool(a2)
print(a1)
print(a2)
print(type(a1))
print(type(a2))

print('----------')

print(a1 + a2)
print(type(a1+a2))