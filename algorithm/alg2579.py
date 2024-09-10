N = int(input())
stairs = list(range(N+3))
for i in range(N):
    stairs[i] = int(input())

# 최댓값 구하기

# 규칙 1 한번에 하나 또는 두개
# 규칙 2 세개연속 X
# 규칙 3 마지막은 무조건 밟

# 부분 문제로 쪼개지나?
# 일단 점화식 세워보자
# 최종 결과가 두가지 형태밖에 나올 수 없음을 생각

# 1) 마지막에 연속으로 올라온 경우 -> i-2는 못밟음. 즉 i-3까지의 최적합에 두개 더함
# 2) 마지막에 한칸 뛰어서 올라온 경우 -> i-2까지에 i번째 더함

dp = stairs.copy()
dp[0] = stairs[0]

dp[1] = dp[0] + stairs[1]
dp[2] = max(stairs[2]+stairs[1], stairs[0]+stairs[2])

for i in range(3, N):
    dp[i] = max((dp[i-3]+stairs[i-1]+stairs[i]), dp[i-2]+stairs[i])
    
print(dp[N-1])
