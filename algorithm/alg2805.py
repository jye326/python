# 나무 인덱스가 아니라 조건을 달성하는 최대의 높이를 계산하는 것
def bin_find(bot, top):
    while(bot<top):
        mid = (bot + top)//2
        if(cal_wood(mid) == M): # 딱 잘렸음 -> 요기반환
            return mid
        elif(cal_wood(mid)>M):# 더 잘렸음-> 좀더 높이 잘라도 됨 -> 하한을 중간보다 높게
            bot = mid + 1
        else:   # 덜 잘렸음 -> 더 낮게 잘라야 함 -> 상한을 중간보다 낮게
            top = mid -1
    if(cal_wood(bot)<M):# 높이 올렸는데 덜 잘린 경우, 아쉽지만 아까 그 값으로 잘라야함
        bot -= 1
    return bot

# 높이가 주어졌을때 모든 나무를 잘라서 얻어지는 값을 계산
def cal_wood(H):
    wood = 0
    for tree in trees:
        if tree > H:#tree가 커터보다 높음
            wood += tree - H
    return wood

N, M = map(int, input().split())
global trees
trees = list(map(int, input().split()))
H = max(trees) # 젤 큰놈
print(bin_find(0, H))
