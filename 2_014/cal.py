#1. 정수와 실수를 사용한 곱셈
n1 = 20
f1 = 3.14
re1 = n1 * f1
print('result1 : {}'.format(re1))
print('result1 : %.2f' %re1)

#2. 문자(열)을 이용한 곱셈
str1 = 'Hi '
re2 = str1 * 7
print('result2 : {}'.format(re2))

#3. 정수와 실수를 사용한 나눗셈 (결과는 항상 float형이다 -> 싫으면 형변환 하셈)
a1 = 10
a2 = 3
re3 = a1 / a2
print('num1 : {}, num2 : {}'.format(a1,a2))
print('result1 : {}'.format(re3))
print('result1 : %.2f' %re3)

#4. 0이 들어간 나눗셈
z = 0
b1 = 3

t1 = z/b1
print('0을 나누는 경우 : {}'.format(t1)) #결과는 항상 0
t2 = b1/z
print('0으로 나누는 경우 : {}'.format(t2)) #오류