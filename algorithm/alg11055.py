N = int(input())
A = list(map(int, input().split()))
dp = list(range(N))
dp[0] = 1
# dp[i] -> A[i]를 포함하는 가장 긴 부분수열의 길이
for i in range(1, N):
    t_max = 0
    for j in range(0, i):
        if A[i]>A[j]:
            t_max = max(t_max, dp[j])
    dp[i] = t_max + 1
print(max(dp))
#이거는 DP로 해결
# 해당 문제는 DP로 못품, 시간 터짐 O(N^2)
