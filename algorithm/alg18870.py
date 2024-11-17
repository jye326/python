# 실패 : 문제를 이해를 못하겠음

import sys
input = sys.stdin.readline
N = int(input())
inputList = list(map(int, input().split()))

sortedList = sorted(list(set(inputList)))
'''
list 중복 제거 방법
set(list())
'''

'''
리스트 정렬 방법 
sorted(list)
역순 정렬
sorted(list, reverse = True)
'''

'''
람다식을 이용한 두번째 키값 기준 정렬
sorted(list, key = {lambda x: x[2]})
'''

dictList = dict(zip(sortedList, list(range(len(sortedList)))))

# set으로 중복 제거하면 없어지는게 맞는데
# 딕셔너리화 해서 제자리에 출력할 수 있음
for x in inputList:
    print(dictList[x],end=" ")
'''
해설 참고
zip -> 두 list의 요소를 묶을 수 있음
dict -> zip으로 묶여있는 요소들을 딕셔너리로 바꿀 수 있음
'''