import sys
N, S = map(int, input().split())
ls = list(map(int, input().split()))

min_length = sys.maxsize
start = 0   #시작ind
current_sum = 0 #현재까지의 합
for end in range(N):
    current_sum += ls[end]
    # 현재 합이 S 이상인 동안 start 포인터를 이동시켜 가장 짧은 길이를 찾음
    while current_sum >= S:
        min_length = min(min_length, end - start + 1)
        current_sum -= ls[start]
        start += 1

if min_length != sys.maxsize:
    print(min_length)
else:
    print(0)


##메모리 초과
# for end in range(0, N):
#     for start in range(0, end+1):
#         dp[start][end] = dp[start][end-1] + ls[end]
#         if dp[start][end] >= S:
#             ans = min(ans, end - start +1)
# if ans != sys.maxsize:
#     print(ans)
# else:
#     print(0)

