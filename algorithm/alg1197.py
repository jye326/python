# 크루스칼 알고리즘, 웨이트 순으로 간선을 정렬하고 작은것부터 union find로 사이클 형성여부를 판단후, 아닐경우에만 트리에 포함

def find(x):
    # X의 대표원소 RETURN
    if unf[x] == x:
        return x
    else:
        unf[x] = find(unf[x])
        return unf[x]
    
def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if rootX<rootY:
            unf[rootY] = rootX
        else:
            unf[rootX] = rootY

# 필요 : 간선을 입력하면 사이클이 형성되는지 확인하는 함수?
# 유니온 파인드 활용, 튜플을 그냥 비교해서 간선에 번호를 매겨서 유니온 파인드? 아니지? 사이클이 만들어지면 안되는거니까?
V, E = map(int, input().split())
global unf
unf = list(range(V+1))    # 노드갯수만큼, 각자의 대표원소, 초기에는 자기 자신
edges = []
for _ in range(E):
    edges.append(tuple(map(int, input().split())))
edges.sort(key= lambda x:x[2])#3번째 요소를 기준으로 정렬하기

distance, cnt = 0, 0 # 찾은 간선 갯수
for a, b, value in edges:
    if find(a) != find(b):  # 간선이 사이클을 만들지 않음
        union(a, b) # 유니온
        cnt+= 1
        distance += value
        if cnt>= V-1:
            break

print(distance)