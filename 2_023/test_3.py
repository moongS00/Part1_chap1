#1부터 100까지의 정수 중 2의 배수와 3의 배수를 구분해서 출력하자

n = 1
while n <= 100 :
    if n % 2 == 0:
        print('{}는 2의 배수이다.'.format(n))

    if n % 3 == 0:
        print('{}는 3의 배수이다.'.format(n))

    n += 1