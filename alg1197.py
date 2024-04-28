# 인접리스트를 활용한 그래프 구현
V, E = map(int, input().split())
graph = [[] for i in range(V)]
visited = [False for i in range(V)]
for _ in range(E):
    t = list(map(int, input().split()))
    # 가중치 있는 무방향그래프
    # node : (도착"인덱스", weight)
    node1 = (t[1]-1, t[2])
    node2 = (t[0]-1, t[2])
    graph[t[0]-1].append(node1)
    graph[t[1]-1].append(node2)



for i in range(V):
    print(i, end = ": ")
    for x in graph[i]:
        print(x, end = " ")
    print()