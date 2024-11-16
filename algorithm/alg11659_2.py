N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum = list(range(N+1))
sum[0] = 0
for i in range(1, N+1):
    sum[i] = sum[i-1] + arr[i-1]

for i in range(M):
    start, end = map(int, input().split())
    print(sum[end] - sum[start-1])
