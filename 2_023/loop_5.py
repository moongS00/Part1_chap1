#무한 루프
##조건식에 논리형 데이터를 사용한 무한루프
flag = True
num = 0
sum = 0
while flag :
    num += 1
    sum += num
    print('{}까지의 합은 {}입니다.'.format(num, sum))

    if sum >= 1000:
        flag = False