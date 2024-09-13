N, M = map(int, input().split())
check = [False for _ in range(N+1)]
stack = list()

'''
백트래킹 : dfs 재귀 중 조건이 어긋난 경우 가지치기를 하고 부모 노드로 회귀하는 것
일단 dfs로 해결해 보자
'''

def dfs():
    if len(stack) == M:
        for i in range(len(stack)):
            print(stack[i], end=" ")
        print()
    for i in range(1, N+1):
        if check[i] == False:
            check[i] = True
            stack.append(i)
            dfs()
            stack.pop()
            check[i] = False
            
dfs()