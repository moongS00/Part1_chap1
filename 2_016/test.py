# 아들이 엄마한테 용돈을 받는데, 첫 달에는 200원을 받고 매월 이전 달의 2배씩 인상하기로 했다.
# 12개월째 되는 달에 얼마를 받을 수 있는지 게산해 보자
first = 200
after12month =( (first * 0.01) ** 12) * 100
after12month = int(after12month)
print('12개월 후 용돈 : {}'.format(after12month))

strResult = format(after12month, ',') #원화 형식으로 표현 가능
#format()함수로 형식을 바꾸면 str형으로 변함
print(strResult, '원')

