#operator 모듈
'''
1. 산술 연산자
+ : operator.add()
- : operator.sub()
* : operator.mul()
/ : operator.truediv()
% : operator.mod()
// : operator.floordiv()
** : operator.pow()
'''
import operator
num1 = 8
num2 = 3
print('{} + {} : {}'.format(num1, num2, operator.add(num1, num2)))
print('{} - {} : {}'.format(num1, num2, operator.sub(num1, num2)))
print('{} * {} : {}'.format(num1, num2, operator.mul(num1, num2)))
print('{} / {} : {}'.format(num1, num2, operator.truediv(num1, num2)))
print('{} % {} : {}'.format(num1, num2, operator.mod(num1, num2)))
print('{} // {} : {}'.format(num1, num2, operator.floordiv(num1, num2)))
print('{} ** {} : {}'.format(num1, num2, operator.pow(num1, num2)))

'''
2. 비교 연산자
== : operator.eq()
!= : operator.ne()
> : operator.gt()
>= : operator.ge()
< : operator.lt()
<= :operator.le()
'''
print('{} == {} : {}'.format(num1, num2, operator.eq(num1, num2)))
print('{} != {} : {}'.format(num1, num2, operator.ne(num1, num2)))
print('{} > {} : {}'.format(num1, num2, operator.gt(num1, num2)))
print('{} >= {} : {}'.format(num1, num2, operator.ge(num1, num2)))
print('{} < {} : {}'.format(num1, num2, operator.lt(num1, num2)))
print('{} <= {} : {}'.format(num1, num2, operator.le(num1, num2)))

'''
3. 논리 연산자
and : operator.and_()
or : operator.or_()
not : operator.not_()
'''
flag1 = True
flag2 = False
print('{} and  {} : {}'.format(flag1 , flag2 , operator.and_(flag1, flag2 )))
print('{} or {} : {}'.format(flag1 , flag2 , operator.or_(flag1 , flag2 )))
print('not {} : {}'.format(flag1 ,  operator.not_(flag1)))