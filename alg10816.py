N = int(input())
nlist = list(map(int, input().split()))
M = int(input())
mlist = list(map(int, input().split()))
nlist.sort()

countList = list(range(20000001))
for i in range(len(countList)):
    countList[i] = 0
for i in range(N):
    countList[nlist[i]+10000000]+=1
for i in range(M):
    print(countList[mlist[i]+10000000], end = " ")

