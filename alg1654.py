# def count_len(H):
#     total = 0
#     for line in lines:
#         if H == 0:
#             total = len(lines)
#             break
#         total += line // H
#     return total

# def bin_find(bot, top):
#     while(bot<top):
#         mid = (bot + top)//2
#         if count_len(mid) == N:
#             while(count_len(mid)==N):
#                 mid+=1
#             mid -= 1
#             return mid
#         elif count_len(mid) > N:    # 갯수 초과 -> 더 길게 자를 수 있음
#             bot = mid +1
#         else:
#             top = mid -1
#     return bot

K, N = map(int, input().split())
global lines
lines = list()
for i in range(K):
    lines.append(int(input()))

bot = 1
top = max(lines)
while(bot<=top):
    mid = (bot + top) // 2
    LAN = 0
    for line in lines:
        LAN += line // mid
    if LAN >= N :
        bot = mid + 1
    else:
        top = mid - 1
    
print(top)
