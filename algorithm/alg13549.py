import sys
from collections import deque
N, K = map(int, input().split())
'''
if N>=K: #나보다 뒤에있으면 그냥 걸어서 갈 수 밖에 없음
    print(K-N)
else:
    count = 0
    nextK = int(K/2)
    while(abs(K-N)>=abs(nextK-N)):
        if(K%2==1):
            count+=1
        K=nextK
        nextK = int(K/2)
    count+=abs(N-K)
    print(count)
'''
# BFS를 사용하는 거였다.
# 어제 풀었던 그리디 문제랑 비슷한 줄 알고 비슷하게 풀려다가 틀린 것 같다.
# 이따가 다시 풀어보자.

## 할수있는거 -> 1초 : +1, -1, 0초 : *2
## 최소 도달 시간이니까 BFS사용
# queue사용-> popleft()
'''
q = deque()
q.append([N,0])
# 최초항 N 삽입
# 근데 경우마다 수는 어케세지?
while(len(q)!=0):
    temp = q.popleft()
    n = temp[0]
    count = temp[1]
    if n==K:
        print(count)
        break#찾았따
    q.append([2*n, count])
    q.append([n+1, count+1])
    q.append([n-1, count+1])
'''
# 방문여부체크를 안했음
# 음수로 가는 경우 생각 안했음
q = deque()
q.append([N,0])

visited = set()
visited.add(N)
# 최초항 N 삽입
# 근데 경우마다 수는 어케세지?
while(len(q)!=0):
    temp = q.popleft()
    n = temp[0]
    count = temp[1]
    if n==K:
        print(count)
        break#찾았따
    if 2*n <=100000 and 2*n not in visited:
        q.append([2*n, count])
        visited.add(2*n)
    if n-1 not in visited and n-1>=0:
        q.append([n-1, count+1])
        visited.add(n-1)
    if n+1 <=100000 and n+1 not in visited:
        q.append([n+1, count+1])
        visited.add(n+1)        
    

# 메모리가 왜 터지지?
# case가 100,000 이상으로도 가버리기 때문!! 나올일 없는 case는 미리 차단하자.

# 또 왜틀?
# X-1이 X+1보다 먼저 진행되어야 함. why?
# X*2가 비용이 0이기 때문에 최대한 많이 사용되어야 하는데 100,000을 넘어갔다가 돌아오지 않기 때문에 *2를 많이 쓰려면 -1을 우선적으로 써야 함