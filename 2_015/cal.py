# 나머지 구하기 : %
a1 = 10
a2 = 3
re1 = a1 / a2
re2 = a1 % a2

print('몫 : %f' %re1)
print('나머지 : %f' %re2)

#몫만 구하기 : //
r = a1 // a2
print('몫 : %f' %r)

#나머지와 몫을 한번에 구하기 : divmod() 함수
re3 = divmod(a1, a2)
print('result : {}'.format(re3))
print('몫 : {}'.format(re3[0]))
print('나머지 : {}'.format(re3[1]))