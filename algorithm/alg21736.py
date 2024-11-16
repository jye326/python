'''
헌내기는 친구가 필요해
BFS 탐색문제
좌표 입력받아서 BFS 돌리고 끝날때까지 P만나면 count 증가
'''
from collections import deque
N, M = map(int, input().split())

board = [[] for i in range(N)]

for i in range(N):
    temp = input()
    for j in range(M):
        board[i].append(temp[j])
a, b = 0, 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'I':
            a, b = i, j

# bfs(board, a, b)

check = [[False for _ in range(M)] for i in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# bfs
q = deque()
q.append([a, b])
# 인덱스 유효
def checkInRange(node, N, M):
    return 0<=node[0]<N and 0<=node[1]<M
# 벽이 아님
def checkIsNotWall(node):
    return board[node[0]][node[1]] != 'X'
def checkIsPeople(node):
    return board[node[0]][node[1]] == 'P'
def checkNotVisited(node):
    return check[node[0]][node[1]] == False
count = 0

while(len(q)!=0):
    # 큐에서 꺼냄
    nowX, nowY = q.popleft()
    # 방문 체크
    check[nowX][nowY] = True
    # 주변에 갈수 있는곳 -> 큐에 넣기.(x)아니면 넣기, 인덱스 체크하기
    for i in range(4):
        nextX = nowX + dx[i]
        nextY = nowY + dy[i]
        node = [nextX, nextY]
        if checkInRange(node, N, M) and checkIsNotWall(node) and checkNotVisited(node):
            if checkIsPeople(node):
                count+=1
            check[nextX][nextY] = True
            q.append(node)

if count == 0:
    print('TT')
else:
    print(count)