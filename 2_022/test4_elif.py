'''
#1. 계절을 입력하면 영어로 번역되는 프로그램을 만들어 보자.
print('계절 : 봄, 여름, 가을, 겨울')
season = input('계절 입력 : ')

if  season == '봄':
    print('{} : {}'.format(season, 'Spring'))
elif season == '여름':
    print('{} : {}'.format(season, 'Summer'))
elif season == '가을' :
    print('{} : {}'.format(season, 'Fall'))
elif season == '겨울' :
    print('{} : {}'.format(season, 'Winter'))
else:
    print('검색할 수 없습니다.')
'''

'''
#2. 키오스크에서 메뉴를 선택하면 영수증이 출력되는 프로그램을 만들어보자
print('1.카페라떼(3.5) \t 2.에스프레소(3.0) \t 3.아메리카노(2.0) \t 4.곡물라떼(4.0) \t 5.밀크티(4.3)')
select = int(input('메뉴 선택 : '))
print('-'*20)
if select == 1:
    print('메뉴 : 카페라떼 \n가격 : 3,500원')
elif select ==2:
    print('메뉴 : 에스프레소 \n가격 : 3,000원')
elif select == 3:
    print('메뉴 : 아메리카노 \n가격 : 2,000원')
elif select == 4:
    print('메뉴 : 곡물라떼 \n가격 : 4,000원')
elif select ==5:
    print('메뉴 : 밀크티 \n가격 : 4,300원')
else:
    print('없는 메뉴 입니다.')

print('-'*20)

'''

#3. 자동차 배기량에 따라 세금을 부과한다고 할 때, 배기량을 입력하면 세금이 출력되는 프로그램을 만들어보자.
my_car = int(input('자동차 배기량 입력 : '))

if my_car < 1000 :
    print('세금 : 100,000원')
elif my_car < 2000 :
    print('세금 : 200,000원')
elif my_car < 3000 :
    print('세금 : 300,000원')
elif my_car < 4000 :
    print('세금 : 400,000원')
elif my_car < 5000 :
    print('세금 : 500,000원')
elif my_car >= 5000 :
    print('세금 : 600,000원')