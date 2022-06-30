#1. 출퇴근 교통수단에 따른 세금 감면 프로그램 제작
select_num = int(input('출퇴근 대상자 인가요? 1.Yes \t 2.No'))

if select_num == 1:
    print('교통수단을 선택하세요')
    tr = int(input('1.도보,자전거 \t 2.버스,지하철 \t 3.자가용'))

    if tr == 1:
        print('세금 감면 5%')
    elif tr == 2:
        print('세금 감면 3%')
    elif tr == 3:
        print('추가 세금 1%')

elif select_num == 2:
    print('세금 변동 없습니다.')

else:
    print('잘못 입력했습니다.')