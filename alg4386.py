import math
def find(x):
    if x == unf[x]:
        return unf[x]
    else:
        unf[x] = find(unf[x])
        return unf[x]
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX < rootY:
        unf[rootY] = rootX
    else:
        unf[rootX] = rootY

def dist(star1, star2):#별 사이 거리 구하기
    return round(math.sqrt(pow(star1[0] - star2[0], 2) + pow(star1[1] - star2[1], 2)), 5)
# n받아서 n^2으로 w 값 다 뽑기
n = int(input())
stars = list()
global unf
unf = list(range(n))# 대표 별
for i in range(n):  # 별들의 위치
    stars.append(tuple(map(float, input().split())))
lines = list()
for i in range(n):
    for j in range(i+1, n):
        lines.append((i, j, dist(stars[i], stars[j])))
lines.sort(key = lambda x : x[2])# w기준 정렬
ans = 0
cnt = 0
for i in lines:
    if find(i[0]) != find(i[1]):
        
        ans += i[2]
        cnt += 1
        union(i[0], i[1])
    if cnt == n -1:
        break
print(round(ans,2))