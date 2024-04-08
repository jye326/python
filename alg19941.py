N, K = map(int, input().split())
line = input()
check = list(range(N))
for i in range(N):
    check[i] = 0
count = 0
for i in range(N):
    if line[i] == 'P':
        for j in range(2*K + 1):
            idx = i-K+j
            if (idx != i) and (idx >= 0) and (idx < N): #자기자신 제외, 유효범위 인덱스
                if(line[idx]=='H' and check[idx] == 0):
                    check[idx] = 1
                    count +=1
                    break
print(count)
        


       
