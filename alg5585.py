price = int(input())
# 낸 건 1000이고 price는 1이상 1000미만
ret = 1000 - price
count = 0 # 동전갯수
while(ret>0):
    if ret >= 500:
        ret -= 500
    elif ret >= 100:
        ret -= 100
    elif ret >= 50:
        ret -= 50
    elif ret >= 10:
        ret -= 10
    elif ret >= 5:
        ret -= 5
    elif ret >= 1:
        ret -= 1
    count+=1    #동전갯수증가
print(count)