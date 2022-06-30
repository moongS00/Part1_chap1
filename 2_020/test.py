#1. 백신접종 대상자는 20세 미만 또는 65세 이상자에 한합니다. 를 논리연산자를 이용해서 코딩해보자.
import operator

age = int(input('나이 입력 : '))
vaccine = operator.or_(operator.lt(age, 20), operator.ge(age, 65))
print('age : {} , result : {}'.format(age, vaccine))

#2. random과 operator 모듈을 사용해서 10부터 100사이의 난수 중 십의 자리와 일의 자리가 각각 3의 배수인지 판단하는 코드를 작성해보자.

import random

ran_int = random.randint(10, 100) #10~100사이의 난수 하나를 뽑음

num10 = operator.floordiv(ran_int, 10)
num1 = operator.mod(ran_int,10)

print('난수 : {}'.format(ran_int))
print('십의 자리 : {}'.format(num10))
print('일의 자리 : {}'.format(num1))

print('십의 자리는 3의 배수이다. : {}'.format(operator.mod(num10, 3)== 0 ))
print('일의 자리는 3의 배수이다. : {}'.format(operator.mod(num1, 3)== 0 ))
