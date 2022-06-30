''''#비교 연산자_숫자 비교 : 결과는 bool
num1 = int(input('첫 번째 숫자 입력 : '))
num2 = int(input('두 번째 숫자 입력 : '))

print('{} > {} : {}'.format(num1, num2, (num1 > num2)))
print('{} >= {} : {}'.format(num1, num2, (num1 >= num2)))
print('{} < {} : {}'.format(num1, num2, (num1 < num2)))
print('{} <= {} : {}'.format(num1, num2, (num1 <= num2)))
print('{} == {} : {}'.format(num1, num2, (num1 == num2)))
print('{} != {} : {}'.format(num1, num2, (num1 != num2)))
'''
#비교 연산자_문자 비교: 아스키 코드를 이용한 비교연산
cha1 = 'A' #65
cha2 = 'S' #83
print('{} > {} : {}'.format(cha1, cha2, (cha1 > cha2)))
print('{} >= {} : {}'.format(cha1, cha2, (cha1 >= cha2)))
print('{} < {} : {}'.format(cha1, cha2, (cha1 < cha2)))
print('{} <= {} : {}'.format(cha1, cha2, (cha1 <= cha2)))
print('{} == {} : {}'.format(cha1, cha2, (cha1 == cha2)))
print('{} != {} : {}'.format(cha1, cha2, (cha1 != cha2)))

#문자와 아스키코드 변환: ord(),chr()
print('\'A\' -> {}'.format(ord('A')))
print('\'S\' -> {}'.format(ord('S')))

print('65 -> {}'.format(chr(65)))
print('83 -> {}'.format(chr(83)))

#문자열 비교 : 문자열 자체 비교
str1 = 'Hello!'
str2 = 'hello!'
print('{} == {} : {}'.format(str1, str2, (str1 == str2)))
print('{} != {} : {}'.format(str1, str2, (str1 != str2)))