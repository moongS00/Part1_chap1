#1. format함수를 이용한 출력
print('1. format함수를 이용한 출력')
name = '홍길동'
age = 20

print('Name : {}'.format(name))
print('Age : {}'.format(age))

print('Name : {}, Age : {}'.format(name,age)) #순차적으로 출력된다
print('Name : {1}, Age : {0}'.format(name,age)) #인덱스를 사용하면 순서를 바꿀 수 있다

print('나의 이름은 {0}이고, 나이는 {1}살 입니다. {0} 이름은 아버님께서 지어 주셨습니다.'
      .format(name, age))

#2. 형식 문자를 이용한 출력
print(f'\n')
print('2. 형식 문자를 이용한 출력')

'''
%s : 문자열
%d : 정수
%f : 실수 (%.1f %.2f %.3f .....)
'''

print('Name : %s' %name)
print('Age : %d' %age)
print('Name : %s, Age : %d' %(name, age))

print('Pie : %f' %3.14)
print('Pie : %d' %3.14)

a = 1.23456
print('A = : %.1f' %a) #소숫점 이하 개수 조절
print('A = : %.2f' %a)
print('A = : %.3f' %a)
print('A = : %.4f' %a)
