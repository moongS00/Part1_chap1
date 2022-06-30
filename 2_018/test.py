'''
# 자동차의 전장과 전폭을 입력하면 자동차 기계 세차 가능 여부를 출력하는 코드를 작성해보자
# 최대 전장 길이 : 5200mm / 최대 전폭 길이 : 1985mm

max_length = 5200
max_width = 1985
car_length = int(input('전장 길이 입력 : '))
car_width = int(input('전폭 길이 입력 : '))
print('전장 가능 여부 : {}'.format((max_length >= car_length)))
print('전폭 가능 여부 : {}'.format((max_width >= car_width)))
'''

#알파벳을 입력하면 아스키 코드를 출력하는 코드를 작성해보자
user_al = input('알파벳 입력 : ')

print('{} -> {}'.format(user_al,ord(user_al)))

#아스키 코드를 입력하면 문자를 출력하는 코드를 작성해보자
user_ask = int(input('아스키 코드 입력 : '))
print('{} -> {}'.format(user_ask, chr(user_ask)))