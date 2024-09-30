N, M = map(int, input().split())
'''
메모리 넉넉, 시간 넉넉 그냥 노드 수 별로 체크 배열 만들어도 된다.
'''

board = [list() for _ in range(N+1)]
check = [False] * (N+1)

for i in range(M):
    x, y = map(int, input().split())
    board[x].append(y)
    board[y].append(x)
count = 0
def dfs(x):
    for linked in board[x]:
        if not check[linked]:
            check[linked] = True
            dfs(linked)
for i in range(1, N+1):
    if not check[i]:
        count += 1
        dfs(i)
print(count)