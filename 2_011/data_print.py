# 1. 기본 출력 방법
print('1. 기본 출력 방법')
name = 'Hong'
print(name)

age = 20
print(age)

#2. 콤마를 이용한 출력 방법
print('2. 콤마를 이용한 출력 방법')
print('Name : ', name)
print('Age : ', age)

#번외. 줄바꿈 없애기
print('3 * 5 = ', end='') #줄바꿈 없애기
print(3*5)

#3. 포맷 문자열을 이용한 데이터 출력
print('3. 포맷 문자열을 이용한 데이터 출력')
print(f'Name : {name}')
print(f'Age : {age}')
print(f'Name : {name}, Age : {age}')

#4. 특수문자
# \t : 탭
# \n : 개행(줄바꿈)
print('4. 특수문자')
print(f'Name : {name} \nAge : {age}')
