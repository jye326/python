# dfs와 bfs
# 깊이 우선과 넓이 우선 탐색
# 방문할 수 있는 점이 없는 경우 종료
# 번호 작은 것부터 방문
# 입력으로 주어지는 간선은 양방향

# 1. 그래프 구현 2차원 연결리스트로 구현
# 2. stack을 사용해서 DFS 탐색 구현
# 그래프 입력
def dfs_stack(graph:list, start:int, visited:list):
    stack = list()
    stack.append(start)
    while(len(stack)!= 0):
        now = stack.pop()  # 스택에서 꺼내
        if not visited[now]:# 미방문인 경우
            visited[now] = True # 방문처리
            for next in sorted(graph[now], reverse=True):
                if not visited[next]:# 안가본 노드인 경우 넣는다.
                    stack.append(next)
            print(now, end = " ")
# 3. 재귀로 DFS 구현
def dfs_recursion(graph:list, start:int, visited:list):
    visited[start] = True
    print(start, end = " ") 
    for next in sorted(graph[start]):
        if not visited[next]:
            dfs_recursion(graph=graph, start=next, visited=visited)

    

# 4. queue를 사용해서 BFS 탐색 구현
def bfs_queue(graph:list, start:int, visited:list):
    q = list()
    q.append(start)
    while(len(q)!=0):
        now = q.pop(0)
        if not visited[now]:
            visited[now] = True
            for next in sorted(graph[now]):
                if not visited[next]:# 연결된 노드 중 미방문 노드만 큐에 넣기
                    q.append(next)
            print(now, end = " ")



N, M, V = map(int, input().split())

graph = [list() for _ in range(N+1)]
# 맨날 헷갈리니까 그냥 정수 번호 사용할 때는 리스트 한 칸 더 크게 만들고 숫자 그대로 사용하도록 하자.
for _ in range(M):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

visited1 = [False for _ in range(N+1)]
visited2 = [False for _ in range(N+1)]

#dfs_stack(graph=graph, start=V, visited=visited1)
dfs_recursion(graph=graph, start=V, visited=visited1)
print()
bfs_queue(graph=graph, start=V, visited=visited2)

