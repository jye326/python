T = int(input())

global count

for _ in range(T):
    M, N, K = map(int, input().split())
    # 세로 N 가로 M 
    board = [[0 for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        m, n = map(int, input().split())
        board[n][m] = 1
    
    
    li = list()

    def dfs(x,y, li):
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        if board[x][y] == 1:
            board[x][y] = 2#방문쳌
            li.append(0)
        elif board[x][y] == 0:
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M: #인접하고
                if board[nx][ny] == 1:
                    board[nx][ny] = 2
                    dfs(nx, ny, li)
    for i in range(N):
        for j in range(M):
            dfs(i,j, li)
            #돌면서 1이면 인접한애들 (포인트로) 다 2로 변경(방문체크)하고 count+1
            # 0이나 2이면 넘어감
    print(len(li))