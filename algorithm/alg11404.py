import sys
inf = sys.maxsize
n = int(input())
m = int(input())
board = [[inf for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    board[i][i] = 0

for i in range(m):
    start, end, dist = map(int, input().split())
    board[start][end] = min(dist, board[start][end])


for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            board[i][j] = min(board[i][j], board[i][k]+board[k][j])

def print_map():
    for i in range(1, n+1):
        for j in range(1, n+1):
            if board[i][j] < inf:
                print(board[i][j], end=' ')
            else:
                print(0, end= ' ')
        print()




print_map()


