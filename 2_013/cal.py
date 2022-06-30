'''
산술 연산자: +, -, *, /, %, //, **
할당 연산자: =, +=, -=. *=, /=, %=, //=
비교 연산자: >, >=, <, <=, ==, !=
논리 연산자: and, or, not
'''

#1. 정수를 이용한 덧셈, 뺄셈
a1 = 9
a2 = 3

re1 = a1 + a2
r1 = a1 - a2
print(f'result1(덧셈) : {re1}')
print(f'result1(뺄셈) : {r1}')

#2. 실수를 이용한 덧셈, 뺄셈
b1 = 3.14
b2 = 0.12

re2 = b1 + b2
r2 = b1 - b2
print(f'result2(덧셈) : {re2}')
print('result2(덧셈) : %.2f' %re2)
print(f'result2(뺄셈) : {r2}')

#3. 정수와 실수를 이용한 덧셈, 뺄셈
re3 = a1 + b2
r3 = a1 - b2

print(f'result3(덧셈) : {re3}')
print(f'result3(뺄셈) : {r3}')

#4. 문자를 이용한 덧셈 (뺄셈은 불가)
s1 = 'Good'
s2 = ' '
s3 = 'morning'

re4 = s1 + s2 + s3
print('result4 : %s' %re4)

#5. 숫자와 문자를 이용한 덧셈 -> 불가능
