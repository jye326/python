"""
쉬운 최단거리
bfs q 사용하자
메모리 좀 더 쓰겠지
메모리 충분할 듯
큐에다가 인덱스 하우상좌 해가지고 빌때까지 pop해서 보드에 count값 적기
"""
from collections import deque
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

# 초기 거리
dist = 0

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            x, y= i, j
            break


# bfs 초기화
q = deque()
q.append([x,y, dist])
board[x][y] = 0 # 시작점이니까 0처리
# 가장 중요한 방문 체크는?
# 2차원 배열을 만들자
check = [[False for _ in range(m)] for _ in range(n)]

while(len(q) != 0):
    nowX, nowY, nowDist = q.popleft()
    check[nowX][nowY] = True
    # 하 우 상 좌
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    # 주변 확인 후 미방문이고 1이면 현재 거리 +1을 해주자
    for i in range(4):
        nX = nowX + dx[i]
        nY = nowY + dy[i]
        if 0<=nX<n and 0<=nY<m: # 인덱스 범위 체크
            if check[nX][nY] == False and board[nX][nY] != 0:
                check[nX][nY] = True
                board[nX][nY] = nowDist +1
                q.append([nX, nY, nowDist+1])

# 원래 갈 수 check 안된애들중에 1인애들을 -1로 바꿔주면 되나?
for i in range(n):
    for j in range(m):
        if check[i][j] == False and board[i][j] == 1:
            board[i][j] = -1

for i in range(n):
    for j in range(m):
        print(board[i][j], end = " ")
    print()