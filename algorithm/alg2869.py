A, B, V = map(int, input().split())
if A == V:
    print(1)
else:
    one_day_after = A - B   # 하루지나고 올라간 위치
    if (V-A) % one_day_after == 0:
        total = (V-A) // one_day_after + 1
    else:
        total = ((V-A) // one_day_after) + 2
    print(total)
    
