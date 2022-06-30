# A if 조건식 else B -> 조건식이 True면 A실행, 아니면 B실행.
num1 = 10
num2 = 100

res = True if num1 > num2 else False
print('num1 > num2 : {}'.format(res))

print('num1은 num2보다 크다.')if res else print('num1은 num2보다 크지않다.')