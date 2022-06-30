#for문이 적합한 경우 -> 횟수에 의한 반복인 경우
#1~10 까지 합 출력
##for문
sum = 0
for i in range(1, 11):
    sum += i

print('sum : {}'.format(sum))

##while문
sum1 = 0
n = 0
while n < 11:
    sum1 += n
    n += 1

print('sum1 : {}'.format(sum1))

#while문이 적합한 경우 -> 조건에 의한 반복인 경우
# 1부터 시작해 7의 배수의 합이 50 이상인 최초의 정수 출력

##for문
tot = 0
max_int = 0

for i in range(1, 101):
    if i % 7 == 0 and tot <= 50:
        tot += i
        max_int = i

    print('i : {}'.format(i))

print('7의 배수의 합이 50 이상인 최초의 정수 : {}'.format(max_int))

##while문
sum = 0
max_int = 0
n = 1

while n <= 100 and sum <= 50:
    n += 1

    if n % 7 == 0 :
        sum += n
        max_int = n

    print('n : {}'.format(n))

print('7의 배수의 합이 50 이상인 최초의 정수 : {}'.format(max_int))