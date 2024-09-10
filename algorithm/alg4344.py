T = int(input())
for _ in range(T):
    li = list(map(int, input().split()))
    N = li[0] # 해당 케이스의 전체 학생수
    avg = (sum(li) - N) / N
    winner = 0
    for i in range(1, N+1):
        if(li[i]>avg):
            winner+=1
    print("{:.3f}%".format((winner/N) * 100))
