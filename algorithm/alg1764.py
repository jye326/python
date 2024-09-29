import sys
input = sys.stdin.readline

N, M = map(int, input().split())
DDlist = set()

DDBDlist = list()

for i in range(N):
    DDlist.add(input().rstrip())
for i in range(M):
    temp = input().rstrip()
    if temp in DDlist:
        DDBDlist.append(temp)

DDBDlist.sort()
print(len(DDBDlist))
for x in DDBDlist:
    print(x)