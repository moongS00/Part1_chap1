'''
자동차 바퀴가 한번 구를때마아 0.15mm씩 마모된다고 한다
현재의 바퀴 두께가 30mm이고 최소 운행 가능 바퀴 두께가 20mm라고 할 때
앞으로 구를 수 있는 획수를 구해보자
'''

cur_thick = 30
rotaton = 0
remo_thick = 0.15

while cur_thick >= 20:
    cur_thick -= remo_thick
    rotaton += 1

print('운행 가능 횟수 : {}'.format(rotaton-1))