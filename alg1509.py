# 지난번에 DP 팰린드롬 했었는데 그거 응용 같음
import sys
line = str(input())
N = len(line)
dp = [[0 for _ in range(N)] for __ in range(N)]
# dp[여기부터][여기까지]가 팰린드롬 -> 1
# line j부터 i까지가 팰린인가?
for i in range(N):
    for j in range(i+1):
        length = i - j
        if length == 0:#길이 1
            dp[j][i] = 1
        elif length == 1:
            if line[j] == line[i]:
                dp[j][i] = 1
        else:
            if line[j] == line[i] and dp[j+1][i-1] == 1:
                dp[j][i] = 1
# 0번째부터 각 end위치까지의 최소 분할수를 min_cut에 저장
min_cut = [2500 for _ in range(N+1)]
min_cut[-1] = 0
for end in range(N):
    for start in range(end+1):
        if dp[start][end] == 1: # start-end가 P임
            min_cut[end] = min(min_cut[end], min_cut[start-1]+1)    # 기존 값과 0-start구간 최솟값+start-end구간(1)을 비교
        
print(min_cut[-2])




# 구간별 팰린드롬 여부는 확인할 수 있음
# 분할 갯수의 최솟값이라는게 뭐지?
