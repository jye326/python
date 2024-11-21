N, M = map(int, input().split())
map1 = [list(map(int,input().split())) for _ in range(N)]
map2 = [list(map(int,input().split())) for _ in range(N)]
for i in range(N) :
    for j in range(M):
        print(map1[i][j]+map2[i][j], end = " ")
    print()