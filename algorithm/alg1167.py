import sys
sys.setrecursionlimit(10**5)
n = int(input())
tree = [[] for _ in range(n+1)]
for i in range(n):
    temp_list= list(map(int, input().split()))
    a = temp_list[0]    # 상위노드
    for j in range(1, len(temp_list)-1, 2):
        b = temp_list[j]
        w = temp_list[j+1]
        tree[a].append([b, w])

start_node = 1
sum_w = 0

dist = [-1] * (n+1)
dist[start_node] = 0

def dfs(start_node, sum_w):
    for node in tree[start_node]:
        s, w = node #이러면 나눠서 들어감
        if(dist[s] == -1):#미방문 노드만
            dist[s] = sum_w + w
            dfs(s, w+sum_w)

dfs(1, 0)

start_node = dist.index(max(dist))

dist = [-1] * (n+1)
dist[start_node] = 0
dfs(start_node=start_node, sum_w=0)
print(max(dist))