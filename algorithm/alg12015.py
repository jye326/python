def binsearch(left, right, target):
    mid = 0
    while(left<right):
        mid = int((left+right)/2)
        if(lis[mid] < target):
            left = mid+1
        else:
            right = mid
    return right

N = int(input())
A = list(map(int, input().split()))
# how 이분탐색?
# 주어진 배열의 인덱스를 하나씩 살펴보면서
# 다음 숫자가 들어갈 위치를 이분탐색해서 리스트 LIS 에 집어넣는다
global lis
lis = list()
lis.append(A[0])
i = 1
while(i<N):
    if(lis[-1]<A[i]):
        lis.append(A[i])
    else:
        pos = binsearch(0, len(lis), A[i])
        lis[pos] = A[i]
    i+=1
print(len(lis))