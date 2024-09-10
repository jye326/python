T = int(input())
for _ in range(T):
    k = int(input())
    n = int(input())
    # k층 n호 구하기
    # 0층 만들기 총 n호수
    dp = list(range(n+1))
    for i in range(1, k+1): #k층까지 가자
        for j in range(1, n+1):
            dp[j] = dp[j-1] + dp[j]
    print(dp[n])
