#while문 (조건에 의한 반복)
end_num = 10
n = 0

while n <= end_num:
    print(n)
    n += 1


#구구단 만들기
a = 1
while a < 10:
    res = 7 * a
    print('{} * {} = {}'.format(7, a, res))
    a += 1

# 다른 조건, 반복문 처럼 pass사용 가능
while b < 10:
    pass
