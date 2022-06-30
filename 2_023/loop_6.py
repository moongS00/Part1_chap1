# 반복문 제어1. continue : 실행을 생략하고, 맨 처음으로 넘어간다
for i in range(100):
    if i % 7 != 0:
        continue    #i가 7의 배수가 아니라면, continue를 만나 처음으로 간다 print는 생략된다.
    print('{}는 7의 배수입니다.'.format(i))



# 반복문 제어2. else : 반복문이 종료된 후 실행된다
cnt = 0
for i in range(100):
    if i % 7 != 0:
        continue
    print('{}는 7의 배수입니다.'.format(i))
    cnt += 1
else:
    print('99까지의 정수 중 7의 배수는 {}개 입니다.'.format(cnt)) #위의 for문이 다 종료된 후에 실행된다

#반복문 제어3. break : 반복문을 빠져나온다
num = 0
while True:
    print('Hello~')
    num += 1

    if num >= 5:
        break

print('The End!')

#1~100까지 정수를 더할 때, 합계가 100이 넘는 최초의 정수 찾기
sum = 0
first_num = 0

for i in range(1, 101):
    sum += i

    if sum > 100:
        first_num = i
        break

print('최초의 정수 : {}'.format(first_num))

