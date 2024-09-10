# N, M 입려
N, M = map(int, input().split())
# 2차원 맵 입력
map = list()
for i in range(N):
    line = input()
    map.append(line)
# 방문여부 체크 배열 생성
check = [[[False for k in range(2)] for i in range(M)] for j in range(N)]
print(check)
