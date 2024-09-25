import sys
INF = sys.maxsize

def test():
    N, M, W = map(int, input().split())
    # N-지점, M - 도로갯수, W-웜홀갯수
    # 도로정보 맵 초기화
    dist = [[INF for _ in range(N+1)] for _ in range(N+1)]
    # 도로정보 : 출발, 도착, 시간
    for _ in range(M):
        S, E, T = map(int, input().split())
        dist[S][E] = min(dist[S][E], T)
        dist[E][S] = min(dist[E][S], T)
    # dp로 각 지점별 최소 거리만들기 : 플루이드 - 워셜


    for k in range(1, N+1):# 0을 거쳐서 가는 경우
        for i in range(1, N+1):
            for j in range(1, N+1):
                    if i!=j:
                        dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
   

    # print('도로거리')
    # for i in range(1,N+1):
    #     for j in range(1,N+1):
    #         if dist[i][j] == INF:
    #             print('%', end = " ")
    #         else:
    #             print(dist[i][j], end=" ")
    #     print() 
    
    

   
   

     # 워프맵
    wdist = [[-INF for _ in range(N+1)] for _ in range(N+1)]    

    # 웜홀정보 : 출발, 도착, back시간
    for _ in range(W):
        WS, WE, WT = map(int, input().split())
        wdist[WS][WE] = WT

    # for k in range(1, N+1):
    #     for i in range(1, N+1):
    #         for j in range(1,N+1):
    #                 if i!=j:
    #                     wdist[i][j] = max(wdist[i][j], wdist[i][k]+wdist[k][j])
    
    # print("워프거리")
    # for i in range(1,N+1):
    #     for j in range(1,N+1):
    #         if wdist[i][j] == -INF :
    #             print('-%', end = " ")
    #         else:
    #             print(wdist[i][j], end=" ")
            
    #     print()
    
    for i in range(1, N+1):
        for j in range(1, N+1):
            if wdist[i][j]!=0 and wdist[i][j]!=INF:
                if wdist[i][j]>dist[i][j]:
                    # print(i, j)
                    print('YES')
                    return
    print('NO')
    return
                

# 1. WE의 S랑 E를 뒤집은 녀석의 도로거리 최소합 > WE값 ->이걸 모든 W에 대해서 ?
    
    
# 도로는 방향이 없고, 같은 지점을 연결하는 도로가 한개 이상일 수 있다.

T = int(input())
for _ in range(T):
    test()