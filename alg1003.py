dp = [[0,0] for _ in range(41)]
#   [0갯수, 1갯수]
dp[0][0]= 1
dp[1][1] = 1
for i in range(2, 41, 1):
    dp[i][0] = dp[i-1][0] + dp[i-2][0]    #0이나온 횟수 = 직전에서 0이 나온횟수 + 직직전 0이 나온횟수
    dp[i][1] = dp[i-1][1] + dp[i-2][1]
T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N][0], end=' ')
    print(dp[N][1])