def find(x):
    if unf[x] == x: # 내가 대빵
        return x
    else:#나 말고 다른애가 대빵
        unf[x] = find(unf[x])   # 내 대빵을 찾아서 설정
        return unf[x]   # 대빵 반환

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        unf[rootY] = rootX

#union find를 활용한 그룹체킹
N = int(input())
M = int(input())
global unf
unf = list(range(N))
for i in range(N):# 도시별 연결정보확인
    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if temp[j] == 1: # i와 temp[j]가 서로 연결
            union(i, j)
ans = list(map(int, input().split()))
base_root = find(ans[0]-1)
y = True
for x in ans:
    if find(x-1) != base_root:
        y = False
        break
if y == True:
    print("YES")
else:
    print("NO")
