N = int(input())
before = list(map(int, input().split()))
print(sum(before)*100/max(before)/N)
