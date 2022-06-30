'''
#1. 1부터 100까지의 정수 중 3과 7의 공배수와 최소 공배수를 출력하자

min_num = 0

for i in range(1,101):
    if i % 3 != 0 or i % 7 != 0:
        continue

    print('공배수 : {}'.format(i))

    if min_num == 0:
        min_num = i

else:
    print('최소 공배수 : {}'.format(min_num))
'''
'''
#2. 10의 팩토리얼을 계산하는 과정에서 결과값이 50을 넘을 때의 숫자를 구하자
res = 1
num = 0

for i in range(1, 11):
    res *= i

    if res > 50:
        num = i
        break

print('num : {}, result : {}'.format(num, res))
'''

#3. 새끼 강아지 체중이 2.2kg이 넘으면 이유식을 중단하려고 한다.
#한번 이유식을 먹을때 체중이 70g증가한다고 할때,
#예상되는 이유식 날짜를 구하자. (현재 체중은 800g 이다)

cur_weight = 800
limit_weight = 2200
date = 1

while True:
    if cur_weight >= limit_weight:
        break

    cur_weight += 70
    date += 1

print('이유식 중단 날짜 : {}'.format(date))