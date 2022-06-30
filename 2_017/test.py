# 연간 누적 강수량 구하기
rain_amount = 0
total_rain = 0

total_rain += 30
print('1월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 45
print('2월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 47
print('3월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 55
print('4월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 65
print('5월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 100
print('6월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 128
print('7월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 209
print('8월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 204
print('9월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 186
print('10월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 67
print('11월 누적 강수량 : {}mm'.format(total_rain))

total_rain += 12
print('12월 누적 강수량 : {}mm'.format(total_rain))
print('-'*30)
print('연간 누적 강수량 : {}mm'.format(total_rain))
print('연간 평균 강수량 : %.2fmm' %(total_rain/12))
print('-'*30)