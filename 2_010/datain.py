# input()함수로 데이터 입력받기
'''
print('키보드를 통해서 데이터를 입력하세요.')
userInputData = input()

print(userInputData)
'''
#--------------------------------------------------------------------------
userInputData = input('키보드를 통해서 데이터를 입력하세요.')

print(userInputData)
print(type(userInputData))
# input()으로 받은 모든 데이터는 항상 문자(열)

#--------------------------------------------------------------------------
#입력받은 데이터의 형 변환하기
print('<입력받은 데이터를 정수로 변환하기>')
k = int(input('정수를 입력 하세요 : '))

print(k)
print(type(k))