#하루에 독감으로 병원에 재방하는 환자 수가 50명에서 100명 사이일 때,
#누적 독감 환자 수가 최초 10000명을 넘는 날짜를 구해보자

import  random

sum = 0
date = 1
flag = True

while flag:
    patient_count = random.randint(50, 100)
    sum += patient_count
    date += 1
    print('날짜 : {}\t  오늘 환자 수 : {}\t  누적 환자 수 : {}\t'.format(date, patient_count, sum))

    if  sum >= 10000:
        flag = False