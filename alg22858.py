N, K = map(int, input().split())
S = list(map(int, input().split()))
D = list(map(int, input().split()))
answer = S.copy()
for i in range(K):
    temp = list(range(N))   # N칸짜리 임의 list 생성
    for j in range(N):
        temp[D[j]-1] = answer[j]  # D[j]의 인덱스에 해당 위치 원소 배치하기
    answer = temp   #temp랑 temp.copy()랑 뭐가 다르지
for i in answer:
    print(i, end=" ")