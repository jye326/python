# 요세푸스 문제
# N개의 배열 만들고, K번 진행을 count한다.
# 뽑힌애들은 0으로 바꾸고, 0인애들이 K번 진행할때 0인 애들은 count안한다.
# 나오는 순서대로 리스트에 담아 출력.

N, K = map(int, input().split())
table = list(range(N+1))#1번부터 넣을꺼
idx = 1#확인하는 인덱스
count = 1
answer = list()
while(len(answer)<N):
    if table[idx] != 0:
        if count == K:  #도착
            answer.append(table[idx]) #정답에 추가
            table[idx] = 0 #빼
            count = 1# count돌리기
        else:
            count+=1
    idx += 1
    if idx > N:
        idx = 1
print('<', end = "")
for i in range(len(answer)-1):
    print(answer[i], end = ", ")
print(answer[N-1], end = '>')