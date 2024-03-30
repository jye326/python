import sys

def binSearch(target):#arr[target]과 가장 0에가까운 용액찾기
    min = sys.maxsize   # 합의 최소 -> target과의 합
    start = target + 1  #target의 다음칸부터 탐색
    end = len(arr)-1    #맨 끝부터 탐색
    while start<end:
        temp = arr[target] + arr[start] + arr[end]
        if abs(temp) < min:
            min = abs(temp)
            answer = target, start, end
        if temp == 0:
            break
        if temp < 0:    #음수 -> 오르쪽으로 start 옮기기
            start += 1
        else:#양수 -> 왼쪽으로 end 옮기기
            end -= 1
    return answer

def sumArr(arr1):   #인덱스의 리스트를 받아서 arr의 합 반환ㄴ
    return arr[arr1[0]] + arr[arr1[1]] + arr[arr1[2]]

N = int(input())
global arr
arr = sorted(list(map(int, input().split())))
min = abs(sumArr(binSearch(0)))   # 3개의 합 절댓값
answer = binSearch(0)   # 일단 정답을 요걸로

for i in range(1, N-2):
    if sumArr(binSearch(i)) == 0:
        answer = binSearch(i)   # 정답!
        break
    if abs(sumArr(binSearch(i))) < min:
        min = abs(sumArr(binSearch(i)))
        answer = binSearch(i)   # 더 작은 값이 있으니 정답 갱신


for i in answer:
    print(arr[i] , end = " ")

