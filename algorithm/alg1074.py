'''
재귀함수 작성 문제
N==1일때 
인덱스 위치부터 Z자 순서로 숫자 새기기
N>1 일때 N-1, N-1부터 Z자로 인덱스 4등분해서 재귀 돌리기
'''
# 메모리 터짐 -> 굳이 배열을 찾지 말고 목표한 인덱스가 나올때 멈추면 되겠다?
# 시간 터짐 why? 더빨리 구할 수 있다고? -> 모든 칸을 한번씩 방문하므로 O(N^2)
# global count
# def Z(N, x, y):
#     global count
#     dx = [0, 0, 1, 1]# + : 아래
#     dy = [0, 1, 0, 1]# + : 오른쪽
#     if N == 1:
#         for i in range(4):
#             tempX = x+dx[i]
#             tempY = y+dy[i]
#             if tempX == r and tempY == c:
#                 print(count)
#                 return
#             count+=1
#     else:
#         for i in range(4):
#             Z(N-1, x+dx[i]*pow(2, N-1), y+dy[i]*pow(2, N-1))
        
# N, r, c = map(int, input().split())
# count = 0
# Z(N, 0, 0)

N, r, c = map(int, input().split())
ans = 0
while N != 0:
    N-=1
    # 첫번째 사분면
    if r<2**N and c < 2**N:
        ans += (2**N) * (2**N) * 0
    # 두번째 사분면
    elif r<2**N and c >=2**N:
        ans += (2**N) * (2**N) * 1
        c -= (2**N) # 다음 재귀를 위해 col 영역을 땡겨옴
    # 세번째
    elif r>=2**N and c <2**N:
        ans += (2**N) * (2**N)*2
        r-= 2**N# 다음 재귀를 위해 row 영역을 땡겨옴
    else:
        ans += (2**N)*(2**N)*3
        r-=(2**N)
        c-=(2**N)
print(ans)