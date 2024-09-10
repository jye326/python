import sys
ans=INF=10**9
ld=lambda:[[INF for _ in range(5)] for _ in range(5)]
k=[0]+[*map(int,sys.stdin.readline().split()[:-1])]
d=[ld()]    
d[0][0][0]=0 #[input][왼발][오른발] = 누적합
x=[[0,2,2,2,2],[0,1,3,4,3],[0,3,1,3,4],[0,4,3,1,3],[0,3,4,3,1]] #0~4 -> 0~4 비용 -> 비용을 이런식으로 저장해놓고 돌리는구나
for i in range(1,len(k)):
    now=k[i]
    d.append(ld())  # dp테이블 맨 뒷열추가
    for l in range(5):  # l 일단 고정
        for p in range(5):  # p 한번씩 밟기
            d[i][l][now] = min(d[i-1][l][p]+x[p][now], d[i][l][now])
            # 그니까 왼발은 고정이고, 이번엔 오른발로 밟을 건데, 오른발이 어디서 출발하는지 결정-> 최소비용 저장
            d[i][now][l] = min(d[i-1][p][l]+x[p][now], d[i][now][l])
            # 오른발이 고정이고, 왼발로 밟을 건데 왼발이 어디서 출발하는지 결정 -> 최소비용 저장

for i in d[-1]: ans=min(ans,min(i))
print(ans)

#내가 짠건 아니고 그냥 공부한 코드