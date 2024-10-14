'''
최단거리 : BFS활용
큐에 좌표 넣고 방문 체크하면 가장 빠른 시간이 T 나옴

일단 가장 빠른 시간부터 찾아볼까

근데 가장 빠른 시간으로 찾는 방법?
모든 방법을 시도해보고 시간이 T면 count++할까?
이게 되네?
'''

from collections import deque
N, K = map(int, input().split())
q = deque()
check = [False] * 200001    # *2로 넘어 갔다 오는 경우때문에 20만으로 설정
# 첫 위치 삽입
q.append([N, 0])

# 방문체크
check[N] = True

def idx_range(n):
    return 0<=n<=200000

if N >= K:
    # 수빈이가 앞서있는 경우
    # 최단거리는 뒤로 쭉 걷는 경우 밖에 없음
    min_time = N-K
    count = 1
else:
    #(N<K)
    min_time = 0
    while(len(q)!=0):
        now, time = q.popleft()
        check[now] = True
        if now == K:    # 도착
            # 최소시간 설정 후 bfs 종료
            min_time = time
            break
        else:
            # 2배가 범위 이내 and 미방문
            if idx_range(now*2) and not check[now*2]:
                # 2배 추가, 시간 1초
                q.append([2*now, time+1])
            if idx_range(now+1) and not check[now+1]:
                q.append([now+1, time+1])
            if idx_range(now-1) and not check[now-1]:
                q.append([now-1, time+1])
    
    # 재시작
    q.clear()
    check = [False] * 200001    # 다시 초기화
    # 첫 위치 삽입
    q.append([N, 0])
    # 방문체크
    check[N] = True
    count = 0
    while(len(q)!=0):
        now, time = q.popleft()
        if time <= min_time:
            check[now] = True
            if now == K:    # 도착
                # 최소시간 내에 도착했으니 숫자 올림
                count+=1
            else:
                # 2배가 범위 이내 and 미방문
                if idx_range(now*2) and not check[now*2]:
                    # 2배 추가, 시간 1초
                    q.append([2*now, time+1])
                if idx_range(now+1) and not check[now+1]:
                    q.append([now+1, time+1])
                if idx_range(now-1) and not check[now-1]:
                    q.append([now-1, time+1])

print(min_time)
print(count)