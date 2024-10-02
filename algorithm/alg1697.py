import sys
from collections import deque
N, K = map(int,input().split())



'''
x+1, x-1, 2*x임 똑같이 1초
-> 가중치가 똑같으니까 BFS를 사용해도 될까?

나보다 뒤에 있을수도 있음
100,000 넘어가거나 0보다 작아지는 경우 제외하기
*2, -1, +1
*2가 많이 이동 > 자주 쓰려면 -1이 먼저와야할 것같음?
데크로 큐 만들고 큐 빌때까지 현재 위치와 count, 방문체크해야되는데 ㅇㅎ
100000만 배열 만들고, 방문체크 -> 다음 행동 후 큐에 넣기 -> 방문해제는 안하나? 안해도 될듯? 이미 다른 방법으로 방문한 지점을 추후에 (더 시간을 쓰면서) 방문할 필요 없음. 최단경로니까
'''

def index_condition(x):
    return 0<=x<=200000

q = deque()
check = [False for _ in range(200001)]
check[N] =  True
q.append((N,0)) #출발점, 시간


if N >= K:
    print((N - K))
else:    
    while(len(q)!= 0):  
        now, count = q.popleft()
        if index_condition(now):
            if now == K:
                print(count)
                break
            else:
                if index_condition(2*now) and now != 0:
                    if not check[2*now]:
                        q.append((2*now, count+1))
                        check[2*now] = True
                if index_condition(now +1):
                    if not check[now +1]:
                        q.append((now +1, count+1))
                        check[now +1] = True
                if index_condition(now -1):
                    if not check[now -1]:
                        q.append((now -1, count+1))
                        check[now -1] = True
            # 순서가 이게 맞나? 순서의 차이를 모르겠음
            
'''
지금처럼 now가 K와 다를때로만 나누지 않고
now가 K보다 작을때와 클때의 동작 순서를 바꾸는게 의미가 있나?
메모리를 최소한으로 쓴게 맞나? -> 5.6Mb가 아니었음, 터짐
'''
'''
애초에 방문 체크를 안함..
했는데 왜 터지지?

50퍼에서 틀림 아마 인덱스 제한을 넉넉하게 잡아야 했나?
2배로 늘렸는데도 틀림.
조건을 다시 확인해보자

N과 K의 대소관계를 나눠놓고 생각하자.

대소관계 처리하고 순서 바꿨는데 50퍼대에서 통과를 못함

그냥 그때그때 now와의 차이를 계산해서 동작 순서를 바꿔야하나?
어차피 근데 BFS면 순서가 의미가 있나?

미친... 범위에 0이 포함되네?

0을 못봄 -> 틀렸을때는 범위 양 끝을 항상 생각하자
'''
    