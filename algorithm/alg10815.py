# 입력
N = int(input())
sangeun = list(map(int, input().split()))
M = int(input())
cards = list(map(int, input().split()))
# 상근이 정렬
sangeun.sort()
for card in cards:
    start = 0
    end = N-1
    flag = False # 찾았냐?
    while(start <= end):
        # mid는 중간 인덱스
        mid =  (start + end)//2
        if sangeun[mid] == card:
            flag = True#찾았다!
            break
        elif sangeun[mid] > card: #중간값이 더 큼 ->아래 절반을 찾자
            end = mid -1
        else:#위 절반 찾자.
            start = mid +1
    if(flag):
        print(1, end = " ")
    else:
        print(0, end = " ")
