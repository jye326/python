'''
recursionError
'''
import sys
sys.setrecursionlimit(1<<30)

N = int(input())
board = list(list() for _ in range(N+1))

for _ in range(N-1):
    fr, to = map(int, sys.stdin.readline().strip().split())
    board[fr].append(to)
    board[to].append(fr) 

# 각 노드별 깊이 저장
arr = [0] * (N+1)

def dfs(cur, prv, cnt):
    # 해당 노드의 깊이
    arr[cur] = cnt
    for nxt in board[cur]:
        if nxt == prv:
            continue
        dfs(nxt, cur, cnt+1)

dfs(1, 0, 0)

cnt = 0
# 리프들의 깊이를 더해준다.
for i in range(2, N+1):
    if len(board[i]) == 1:
        cnt += arr[i]

if cnt % 2 == 1:
    print('YES')
else:
    print('NO')
'''
각 리프노드의 깊이합이 홀수인지 짝수인지
'''