N = int(input())
Tshirt = list(map(int, input().split()))
T, P = map(int, input().split())
count = 0
for i in range(6):
    if 0<Tshirt[i] <= T:
        count += 1
    elif Tshirt[i]>T:
        if Tshirt[i] % T == 0:
            count += Tshirt[i]// T
        else:
            count += (Tshirt[i]//T) +1
print(count)
print(N//P, N % P)