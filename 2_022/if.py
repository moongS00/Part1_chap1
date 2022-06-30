#<제어문>
'''
제어문은 조건문과 반복문 2개로 나뉜다

조건문의 종류
1) if문 : 단일조건
2) if~else문 : 양자택일
3) if~elif문 : 다자택일(다중조건)
'''
#1. if문 : if문이 참이면 실행문을 실행, 거짓이면 실행하지 않는다. (들여쓰기 꼭 하기)
if 10 > 5 :
    print('10은 5보다 크다.')

num1 = 10
num2 = 20
if num1 > num2 :
    print('num1은 num2보다 작거나 같다.') #에러가 나는게 아니고 그냥 실행만 안된다.


#2. if~else문 : 조건식 결과에 따라 둘 중 하나가 실행됨
pass_score = 80
my_score = int(input('점수 입력 : '))

if my_score < pass_score:
    print('FAIL!!')
else:
    print('PASS!!')
'''
실행문이 정해지지 않았을땐 pass라고 하면 오류나지 않음
if my_score < pass_score:
    pass
else:
    pass
'''

#3.if~else문과 조건식
##조건식의 두가지 사용법_1) 조건식 결과에 따른 실행
userpoint = 100
ablepoint = 500
print('포인트 사용 가능') if userpoint >= ablepoint else print('프린트 사용 불가능')

##2) 조건식 결과를 변수에 할당하는 경우
res = '가능' if userpoint >= ablepoint else '불가능'
print('포인트 사용 가능 여부 : {}'.format(res))

#4. if~elif문
exam_score = int(input('시험 성적 입력 : '))
grade = ''

if exam_score >= 90:
    grade = 'A'
elif exam_score >= 80:
    grade = 'B'
elif exam_score >= 70:
    grade = 'C'
elif exam_score >= 60:
    grade = 'D'
else:
    grade = 'F'

print('성적 : {} \t 학점 : {}'.format(exam_score, grade))


#5. 중첩 조건문
if exam_score < 60:
    print('재시험 대상입니다.')

else:
    if exam_score >= 90:
        print('A')
    elif exam_score >= 80:
        print('B')
    elif exam_score >= 70:
        print('C')
    elif exam_score >= 60:
        print('D')
