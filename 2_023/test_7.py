#구구단 전체를 출력해보자

for i in range(1, 10):
    for j in range(2, 10):
        res = i*j
        print('{} * {} = {}\t'.format(i, j, res), end='')
    print()