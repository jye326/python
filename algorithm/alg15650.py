N, M = map(int, input().split())
check = [False for _ in range(N+1)]
stack = list()
def dfs(n):
    if len(stack) == M:
        #print(stack)    #수정필요
        print(' '.join(str(x) for x in stack))
    else:
        for i in range(n,N+1):
            if check[i] == False:
                check[i] = True
                stack.append(i)
                dfs(i+1)
                stack.pop()
                check[i] = False

dfs(1)

