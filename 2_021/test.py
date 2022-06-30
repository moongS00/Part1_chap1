'''
#1. 적설량을 입력하고 적설량이 30mm이상이면 대설 경보를 발령하고 그렇지 않으면 대설 경보를 해제하는 코드를 작성해보자

limit = 30
snow = int(input('적설량 입력(mm) : '))

print('적설량 : {}mm, {}'.format(snow, '대설 경보 발령!')) if snow >= limit else \
    print('적설량 : {}mm, {}'.format(snow, '대설 경보 해제~'))
'''

#2. 국어, 영어, 수학 점수를 입력하면 조건식을 이용해서 과목별 결과와 전체 결과를 출력하는 코드를 작성해 보자.
# 과목별 합격 점수: 60점
# 전체 합격 평균 점수 : 70점

import operator

pass_score1 = 60
pass_score2 = 70

kor_score = int(input('국어 점수 : '))
eng_score = int(input('영어 점수 : '))
mat_score = int(input('수학 점수 : '))

total_score = kor_score + eng_score + mat_score
avg_score = total_score / 3

print('국어 : PASS') if operator.ge(kor_score, pass_score1) else print('국어 : FAIL')
print('영어: PASS') if operator.ge(eng_score, pass_score1) else print('영어: FAIL')
print('수학 : PASS') if operator.ge(mat_score, pass_score1) else print('수학 : FAIL')
print('시험 : PASS') if operator.ge(avg_score, pass_score2) else print('시험 : FAIL')

print('총점 : {}, 평균: {}'.format(total_score , avg_score ))