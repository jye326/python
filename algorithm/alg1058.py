N = int(input())
board = list(list(input()) for _ in range(N))

# 어떤 행의 2-친구 구하는 함수
def friends_2(N, board, row):
    friends_2 = 0
    for i in range(N):
        if board[row][i] == 'Y':
            # 너는 내 친구
            friends_2 += 1
        else:
            if row != i:
                # i는 내 친구가 아니지만
                # 2-친구면 +1
                for j in range(N):
                    if board[row][j] == 'Y' and board[i][j] == 'Y':
                        friends_2 += 1
                        break
    return friends_2
maxNum = 0
for i in range(N):
    maxNum = max(maxNum, friends_2(N=N, board=board, row=i))
print(maxNum)