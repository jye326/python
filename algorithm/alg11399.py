N = int(input())
P = list(map(int, input().split()))
P.sort()
PP = list(0 for _ in range(N))
PP[0] = P[0]
count = P[0]
for i in range(1, N):
    PP[i] = PP[i-1] + P[i]
    count+=PP[i]

print(count)