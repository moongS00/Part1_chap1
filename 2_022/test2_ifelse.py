'''
#1. 나이가 65세 이상이면 교통 요금 무료를 적용하는 프로그램을 만들어 보자
senior = 65
age = int(input('나이 입력 : '))

if age < senior:
    print('유료 대상 승객입니다.')
else:
    print('무료 대상 승객입니다.')
'''

#2. 소숫점 첫번째 자리에서 반올림하는 프로그램을 만들어보자
num = float(input('소수 입력 : '))

if num - int(num) >= 0.5 :
    print('올림 : {}'.format(int(num) + 1))
else:
    print('버림 : {}'.format(int(num)))