'''
# 백신 접종 대상자는 20세 미만 또는 65세 이상자에 한합니다. 를 논리연산자로 코딩해보자
age = int(input('나이 입력 : '))
vaccine = (age < 20) or (age >= 65)
print('age : {}, result : {}'.format(age,vaccine))
'''

#국어, 영어, 수학 점수를 입력하고 평균이 70점 이상이면 True를 출력하는 코드를 작성해보자.
# 과목별 점수가 최소 60 이상인 경우에 True를 출력한다.
score_korean = int(input('국어 점수 : '))
score_english = int(input('영어 점수: '))
score_math = int(input('수학 점수 : ' ))
score_average = (score_korean + score_english + score_math)

standard = 60
standard_average = 70

avg_res = score_average >= standard_average
kor_res = score_korean >= standard
eng_res = score_english >= standard
mat_res = score_math >= standard

print('평균 : {}, 결과 : {}'.format(score_average, avg_res))
print('국어 : {}, 결과 : {}'.format(score_korean, kor_res))
print('영어: {}, 결과 : {}'.format(score_english , eng_res))
print('수학 : {}, 결과 : {}'.format(score_math , mat_res))
print('과락 결과: {}'.format(kor_res and eng_res and mat_res))
print('최종 결과: {}'.format(kor_res and eng_res and mat_res and avg_res))