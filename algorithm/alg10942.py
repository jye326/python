# 어떤 수열이 팰린드롬인지 판별하면 된다.
# 왜 DP지? 그냥 리스트 넣고 돌리면 안되나?
# 시간 제한에 걸리나?

# 문제를 받을때마다 리스트로 확인하면서 판별하면 느릴것같다. 최대 2000번 * 1,000,000 이니까 개느리겠다.
# DP 테이블에 어디부터 어디까지가 팰린드롬인지 저장해놓고, 인덱스로 바로바로 출력하면 빠르긴 하겠다.

# DP 테이블을 어떻게 활용해야 하나?
# 핵심 -> 팰린드롬을 작은 단위부터 쪼갠다.

# 길이가 1 -> 무조건 팰린드롬
# 2 -> 둘이 같으면 팰린드롬
# 3 -> 양쪽이 같으면서 사이가 팰린드롬이면 팰린드롬

import sys
N = int(input())
arr = list(map(int, sys.stdin.readline().split()))
#print(arr)
# DP테이블 할당
ld = lambda:[0 for i in range(N)]
d = [ld()]
for _ in range(N):
    d.append(ld())
# DP테이블 채우기
for i in range(N):  # d[i][j] i도착 j출발
    for j in range(i+1):  
        leng = i - j
        if leng == 0:   #  길이가 1
            d[i][j] = 1 #   팰린드롬
        elif leng == 1:
            if arr[i] == arr[j]:
                d[i][j] = 1 # 팰린드롬
        else:   # 3이상
            if arr[i] == arr[j] and d[i-1][j+1] == 1:
                d[i][j]= 1


M = int(input())
for _ in range(M):
    i, j = map(int,sys.stdin.readline().split())
    if(d[j-1][i-1]==1):
        print(1)
    else:
        print(0)