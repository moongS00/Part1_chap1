'''
range() 기본

for i in range(1, 11, 1)
    : 1부터 10까지 1씩 증가 (증가가 1인 경우, 생략 가능)

for i in range(0, 10, 2)
    : 0부터 9까지 2씩 증가 (시작이 0인 경우, 생략 가능)
'''

#사용자가 반복의 시작과 끝을 입력하면 1씩 증가하는 반복문을 만들어보자
start = int(input('반복의 시작 입력 : '))
end = int(input('반복의 끝 입력 : '))

for i in range(start, (end+1)):
    print(i)