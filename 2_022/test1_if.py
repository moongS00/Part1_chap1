#1. 국어, 영어, 수학 점수를 입력하고 평균이 90점 이상이면 '참 잘했어요.'를 출력하는 코드를 작성하자.
'''
kor_score = int(input('국어 점수 입력 : '))
eng_score = int(input('영어 점수 입력 : '))
mat_score = int(input('수학 점수 입력 : '))

avg_score = (kor_score + eng_score + mat_score ) / 3
print('평균 : {}'.format(avg_score))

if avg_score >= 90 :
    print('참 잘했어요~')
'''

#2. 실내 온도를 입력하고 온도가 28도 이상이면 '냉방 작동!'이 출력되고, 20도 이하면 '난방 작동!'이 출력되는 코드를 작성하자
tem_high = 28
tem_low = 20

tem_now = int(input('실내 온도 입력 : '))

if tem_now >= tem_high:
    print('냉방 작동!')

if tem_now <= tem_low:
    print('난방 작동!')