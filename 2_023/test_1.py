#구구단 만들기
for i in range(9):
    for j in range(9):
        res = (i+1) * (j+1)
        print('{} * {} = {}'.format(i+1, j+1, res))

