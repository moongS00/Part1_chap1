all = int(input('전체 학생 수 : '))
group = int(input('한 모둠 학생 수 : '))

group_count = all//group
over = all % group

print('전체 학생 수 : {}'.format(all))
print('한 모둠 학생 수 : {}'.format(group))
print('모둠 수 : {}'.format(group_count))
print('남는 학생 수 : {}'.format(over))