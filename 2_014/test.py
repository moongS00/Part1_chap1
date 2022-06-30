#1. 국어, 영어, 수학 점수를 입력하고 합계와 평균을 출력해보자.
k = int(input('국어 점수 : '))
e = int(input('영어 점수 : '))
m = int(input('수학 점수 : '))

t = k + m + e

print('국어 점수 {}'.format(k))
print('영어 점수 {}'.format(e))
print('수학 점수 {}'.format(m))
print('합계 {}'.format(t))
print('평균 %.2f' %(t/3))