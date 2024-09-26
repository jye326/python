import sys
from sys import stdin
INF = sys.maxsize

# def test():
#     N, M, W = map(int, input().split())
#     # N-지점, M - 도로갯수, W-웜홀갯수
#     # 도로정보 맵 초기화
#     dist = [[INF for _ in range(N+1)] for _ in range(N+1)]

#     # 초기화 : 자기 자신 거리 0
#     for i in range(1, N+1):
#         dist[i][i] = 0

#     # 도로정보 : 출발, 도착, 시간
#     for _ in range(M):
#         S, E, T = map(int, input().split())
#         dist[S][E] = min(dist[S][E], T)
#         dist[E][S] = min(dist[E][S], T)
#     # dp로 각 지점별 최소 거리만들기 : 플루이드 - 워셜

#     for k in range(1, N+1):
#         for i in range(1, N+1):
#             for j in range(1, N+1):
#                     if i!=j:
#                         dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
   

#     print('도로거리')
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             if dist[i][j] == INF:
#                 print('%', end = " ")
#             else:
#                 print(dist[i][j], end=" ")
#         print() 
    
    
#      # 워프맵
#     wdist = [[-INF for _ in range(N+1)] for _ in range(N+1)]    

#     # 웜홀정보 : 출발, 도착, back시간
#     for _ in range(W):
#         WS, WE, WT = map(int, input().split())
#         wdist[WS][WE] = WT
    
   


#     for k in range(1, N+1):
#         for i in range(1, N+1):
#             for j in range(1,N+1):
#                     if i!=j:
#                         if wdist[i][j] != -INF and wdist[i][k] != -INF and wdist[k][j] != -INF:
#                             wdist[i][j] = max(wdist[i][j], wdist[i][k]+wdist[k][j])

#     print("워프거리")
#     for i in range(1,N+1):
#         for j in range(1,N+1):
#             if wdist[i][j] == -INF :
#                 print('-%', end = " ")
#             else:
#                 print(wdist[i][j], end=" ")
            
#         print()


#     for _ in range(1, N+1):
#         if wdist[i][i] != -INF and wdist[i][i] <0:
#             print('YES')
#             return
    
    
    
#     for i in range(1, N+1):
#         for j in range(1, N+1):
#             if wdist[i][j]!=0 and wdist[i][j]!=INF:
#                 if wdist[i][j]>dist[i][j]:
#                     print('YES')
#                     return
                

    
#     print('NO')
#     return
                

def test():
    N, M, W = map(int, stdin.readline().split())

    edges = []

    for _ in range(M):
        S, E, T = map(int, stdin.readline().split())
        edges.append((S,E,T))   # 도로는 양방향
        edges.append((E,S,T))
    #웜홀 정보
    for _ in range(W):
        WS, WE, WT = map(int, stdin.readline().split())
        edges.append((WS, WE, -WT)) #웜홀은 단방향, 시간을 거꾸로 가므로 -WT
    
    # 벨만 포드 알고리즘 : 음수 사이클 감지
    def bf(start):
        dist = [INF] * (N+1)
        dist[start] = 0
        #N-1번 반복해서 최단 경로를 찾는다.
        for _ in range(N-1):
            for u, v, cost in edges:
                if dist[u] != INF and dist[u] + cost < dist[v]:
                    dist[v] = dist[u] + cost
        # 음수 사이클이 존재하는지 확인한다.
        for u, v, cost in edges:
            if dist[u] != INF and dist[u] + cost < dist[v]:
                return True #음수사이클 존재
        return False
    
    if bf(1):
        print('YES')
    else:
        print('NO')
        

T = int(input())
for _ in range(T):
    test()