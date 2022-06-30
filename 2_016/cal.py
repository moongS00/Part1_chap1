#거듭제곱 : **
a1 = 2
a2 = 3
re1 = a1 ** a2
print('2의 3제곱 : {}'.format(re1))

#n의 m제곱근 구하기 : n ** (1/m)
#2의 제곱근 구하기
q1 = 2 **(1/2)
print('2의 제곱근 %f' %q1)
print('2의 제곱근 %.2f' %q1)

#2의 3제곱근 구하기
q2 = 2 **(1/3)
print('2의 3제곱근 %f' %q2)
print('2의 3제곱근 %.2f' %q2)

#2의 4제곱근 구하기
q3 = 2 **(1/4)
print('2의 4제곱근 %f' %q3)
print('2의 4제곱근 %.2f' %q3)

#sqrt() 함수를 이용한 제곱근 구하기 (2제곱근만 구할 수 있다는 단점 존재)
import math
print('2의 제곱근 %f' %math.sqrt(2))
print('2의 제곱근 %.2f' %math.sqrt(2))
print('2의 3제곱근 %f' %math.sqrt(3))
print('2의 3제곱근 %.2f' %math.sqrt(3))
print('2의 4제곱근 %f' %math.sqrt(4))
print('2의 4제곱근 %.2f' %math.sqrt(4))

#pow() 함수를 이용한 거듭제곱 구하기
print('2의 3제곱 %f' % math.pow(2,3))
print('3의 4제곱 %f' % math.pow(3,4))