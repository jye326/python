def find(x):#unf를 확인, 본인의 대표를 반환함
    if unf[x] == x:#내가 대표
        return unf[x]
    else:#내가 아님
        unf[x] = find(unf[x])# 내 대표를 그놈의 대표로 설정
        return unf[x]
def union(x, y): #두 노드의 대표를 합침, 작은 인덱스가 대표함
    rootX = find(x)
    rootY = find(y)
    unf[rootY] = rootX
# union 정의 똑바로하자
N = int(input())
M = int(input())
global unf
unf = list(range(N))    # 각 컴퓨터의 대표 ind
global lines    #연결선들
lines = list()
for i in range(M):
    lines.append(tuple(map(int, input().split())))
lines.sort(key = lambda x:x[2]) #lines 튜플의 3번째 원소 기준으로 정렬
cnt = 0
ans = 0
for line in lines:
    x = line[0] -1 
    y = line[1] -1
    if(find(x)!=find(y)):# 사이클을 형성하지 않는 경우에만
        union(x,y)# 노드 연결
        ans += line[2]# 정답 추가
        cnt += 1# 숫자 증가
        if(cnt == N-1):
            break
print(ans)