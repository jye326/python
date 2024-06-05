# 입력
T = int(input())
for i in range(T):
    N = int(input())
    # 봤다
    note1 = list(map(int, input().split()))
    note1.sort()
    # 테스트 용지
    M = int(input())
    note2 = list(map(int, input().split()))
    for X in note2:
        start = 0
        end = len(note1)-1
        flag = False
        while(start <= end):
            mid = (start + end) // 2
            if note1[mid]<X:#목표값이 위쪽에 있음
                start = mid +1
            elif note1[mid]>X:
                end = mid -1
            else:
                flag = True
                break
                
        if flag:
            print(1)
        else:
            print(0)



