from collections import deque
# N, M 입려
N, M = map(int, input().split())
# 2차원 맵 입력
map = list()
for i in range(N):
    line = input()
    col = list()
    for x in line:
        col.append(int(x))
    map.append(col)
# 방문여부 체크 배열 생성, -1 = 미방문, 
check = [[[False,False] for _ in range(M)] for _ in range(N)]

queue = deque() # bfs 큐, 방문체크 하고 넣기
max_count = 0
queue.append([0,0, True, 1])
# [x좌표, y좌표, 뚫기권보유, 이동비용]
def bfs():
    #일단 뽑아
    while(len(queue)>0):
        point = queue.popleft()
        x, y, chance, count = point
        

        if chance:
            if check[x][y][1]:
                continue
            else:
                check[x][y][1] = True
        else:
            if check[x][y][0]:
                continue
            else:
                check[x][y][0] = True


        if x == N-1 and y == M-1:
            print(count)
            return
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        for i in range(4):
            X = x+dx[i]
            Y = y+dy[i]
            if not (X<0 or X> N-1 or Y<0 or Y>M-1):#범위설정
                if map[X][Y] == 0:
                    if chance and not check[X][Y][1]:# 기회 있는 미방문
                        queue.append([X, Y, True, count+1])
                    elif not chance and not check[X][Y][0]: # 기회 없는 미방문
                        queue.append([X, Y, False, count+1])
                elif map[X][Y] == 1 and chance: # 벽인데, 기회가 있음
                    if not check[X][Y][0]:# 미방문
                        queue.append([X,Y,False, count+1])

bfs()
if not check[N-1][M-1][0] and not check[N-1][M-1][1]:
    print(-1)