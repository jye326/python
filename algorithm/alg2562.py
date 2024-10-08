ans = 0
idx = 0
for i in range(9):
    x = int(input())
    if x > ans:
        ans = x
        idx = i
print(ans)
print(idx+1)