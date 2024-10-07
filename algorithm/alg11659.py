import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
# dp = [[0 for _ in range(N+1)] for _ in range(N+1)]

# for i in range(1, N+1):
#     dp[i][i] = arr[i-1]
#     for j in range(i, N+1):
#         dp[i][j] = dp[i][j-1] + arr[j-1]

# for _ in range(M):
#     start, end = map(int, input().split())
#     print(dp[start][end])
    
dp = [0 for _ in range(N+1)]
dp[1] = arr[0]
for i in range(2, N+1):
    dp[i] = dp[i-1]+arr[i-1]

for _ in range(M):
    start, end = map(int, input().split())
    print(dp[end]- dp[start-1])

# 뺴면 되네..

