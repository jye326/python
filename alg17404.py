N = int(input())
cost = [list(map(int, input().split())) for i in range(N)]
ans = 1000001
for i in range(3):
    dp = [[1000001 for _ in range(3)] for i in range(N)]
    dp[0][i] = cost[0][i] # 첫 집을 미리 선택 i <---- 이걸 못 떠올림
    for j in range(1, N):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + cost[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + cost[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + cost[j][2]
    for c in range(3):  # 마지막 집 c와 첫집 i를 비교   <---- 이걸 못 떠올림
        if i != c:
            ans = min(ans, dp[-1][c])
print(ans)