N = int(input())
arr = list()
for i in range(N):
    arr.append(input())
# 중복 제거
arr = list(set(arr))
arr.sort()
# 일단 정렬 -> 사전순
arr.sort(key = lambda x : len(x))
# 길이순 정렬
for x in arr:
    print(x)


