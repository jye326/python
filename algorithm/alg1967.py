n = int(input())
graph = [[] for _ in range(n+1)]

def dfs(x, w):
    for start in graph[x]:
        end, dist = start
        if distance[end] == -1:
            distance[end] = w + dist
            dfs(end, w + dist)

# tree 구현
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n+1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾는 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1]*(n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))