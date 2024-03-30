import sys
N = int(input())
arr = sorted(list(map(int, input().split())))
start = 0
end = N-1
min = sys.maxsize
while(start < end):
    temp = arr[start] + arr[end]
    if(abs(temp)<min): # 정답 갱신해야하는 상황
        min = abs(temp) # 최소값 갱신하고,
        answer = arr[start], arr[end] # 지금까지의 정답갱신
    if(temp == 0):
        break
    if(temp < 0): #차이 음수
        start += 1
    else:
        end -= 1 #차이 양수 ->

for x in answer:
    print(x, end = " ")