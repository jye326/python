# 문제 조건을 잘 확인하자. 그냥 3중for문 돌려도 되는 범위였따.
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
sum = 0

count = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i] + arr[j] + arr[k]<=M:
                sum = max(sum, arr[i] + arr[j] + arr[k])

print(sum)
