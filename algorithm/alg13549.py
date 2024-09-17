'''
N, K = map(int, input().split())
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