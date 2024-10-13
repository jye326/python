'''
N이 주어짐
0정사각형, 1정사각형이 각각 몇개 나오는가?
정사각형 size N -> 
check1.사분면 값이 같은가? -> 아무 칸의 숫자 count + 1
사분면이 다른가? -> N/2사이즈로 쪼개고 각 사분면에 대해 check1.수행


1) 필요한 함수
check1) board 값이 전부 같은지 확인후 같으면 아무칸의 숫자 count +1하기
전부 같지 않으면 N/2사이즈로 쪼개고 각 사분면에 대해 재귀
if N == 1 : 
각 칸에 대해 1이면 1count +1 , 0이면 0count +1

입력 : 변의 길이 N, x의 시작 인덱스, y의 시작 인덱스
출력 : X (과정에서 count 함)
전역변수 count_1와 count_0 필요
'''

N = int(input())
board = []
for i in range(N):
    board.append(list(map(int, input().split())))
global count_0
global count_1
count_0 = 0
count_1 = 0
def check1(board,N, idx, idy):
    global count_0
    global count_1

    flag = True # 전부 같을 경우
    standard = board[idx][idy]  # 비교를 위한 첫째항
    for i in range(idx, idx+N):
        if flag == True:
            for j in range(idy, idy+N):
                if board[i][j] != standard:#하나라도 틀리면 끝
                    flag = False
                    break
    
    if flag == True: # 전부 같은 경우 해당 숫자 증가
        if standard == 0:
            count_0 += 1
        else:
            count_1 += 1
    else:
        check1(board, N//2, idx, idy)   #1번 사분면
        check1(board, N//2, idx, idy+N//2)#2번 사분면
        check1(board, N//2, idx+N//2, idy)   #3번 사분면
        check1(board, N//2, idx+N//2, idy+N//2)#4번 사분면
check1(board, N, 0, 0)
print(count_0)
print(count_1)