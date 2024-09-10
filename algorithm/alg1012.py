T = int(input())
# 가로 M 세로 N, K개의 배추 위치
M, N, K = map(int, input().split())
# M by N 맵 생성
field = [[0 for x in range(N)] for y in range(M)]
check = [[False for x in range(N)] for y in range(M)]
for i in range(K):
    x, y = map(int, input().split())
    field[x][y] = 1

q = list() # append pop(0)으로 큐 구현

X = [1, 0, -1, 0]
Y = [0, 1, 0, -1]

for i in range(M):
    for j in range(N):
        #print(field[i][j], end ="")
        if check[i][j] == False and field[i][j] == 1:# 미방문 배추
            check[i][j] = True #방문체크
            for x in range(4):
                
    



# 재귀 X
# 큐가 빌때까지 반복문
# 좌표순서대로 큐에 삽입
# 별도의 체크배열 생성

# 해당 좌표 이미 방문 -> break
# 미방문 -> 방문 체크 후 배추인 경우만
# 주변 좌표 큐에 담아서 우선 탐색 하기
