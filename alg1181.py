N = int(input())
sets = [set() for _ in range(52)]
ls = [list() for _ in range(52)]
for i in range(N):
    word = input()
    sets[len(word)].add(word)
    
for i in range(51):
    if len(sets[i]) != 0:
        ls[i] = sorted(list(sets[i]))
        for x in ls[i]:
            print(x)