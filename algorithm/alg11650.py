N = int(input())
arr = list()
for _ in range(N):
    point = list(map(int, input().split()))
    arr.append(point)
arr.sort(key= lambda x : (x[0], x[1]))
for x in arr:
    print(x[0], x[1])