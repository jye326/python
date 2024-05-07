# mst를 구하고 가장 비싼 길 하나를 딱 끊어버리면 MST 2개로 나뉘지 않을까?
def find(x):
    if boss[x] == x:
        return boss[x]
    else:
        boss[x] = find(boss[x])
        return boss[x]
def union(x, y):
    bossX = find(x)
    bossY = find(y)
    if bossX < bossY:
        boss[bossY] = bossX
    else:
        boss[bossX] = bossY
N, M = map(int, input().split())
line = list()
for i in range(M):
    line.append(tuple(map(int, input().split())))
#길을 weight순으로 정렬
line.sort(key = lambda x : x[2])
# 일단 MST를 구현해야함, Union Find 돌리기
boss = list(range(N))
ans= 0  # 최종정답
maxW = 0 # 최대 유지비
count = 0 #길 갯수
for i in line:
    if find(i[0]-1) != find(i[1]-1):
        ans += i[2]
        maxW = max(maxW, i[2])
        count += 1
        union(i[0]-1, i[1]-1)
    if count >= N-1:
        break
print(ans - maxW)
