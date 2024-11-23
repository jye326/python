from collections import deque
N = int(input())
deq = deque(range(1, N+1))
li = list()
for i in range(N):
    if i % 2 == 0:
        li.append(deq.popleft())
    else:
        li.append(deq.pop())
for x in li:
    print(x, end=" ")