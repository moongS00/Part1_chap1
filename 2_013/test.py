#1. 국어, 영어, 수학 점수를 입력하고 합계를 출력해보자.
'''
k = int(input('국어 점수 : '))
e = int(input('영어 점수 : '))
m = int(input('수학 점수 : '))
t = k + m + e

print('국어 점수 {}'.format(k))
print('영어 점수 {}'.format(e))
print('수학 점수 {}'.format(m))
print('합계 {}'.format(t))
'''
#2. 이번달 알바비와 카드값을 입력하고, 남은 금액이 얼마인지 출력해보자
m = int(input('알바비 입력 : '))
c = int(input('카드값 입력 : '))
r = m-c
print('이번달 알바비 : %d 원' %m)
print('이번달 카드값 : %d 원' %c)
print('남는돈 : %d 원' %r)
