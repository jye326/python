inputString = input()
arr = list()
for c in inputString:
    arr.append(c)
arr.sort(reverse=True)
for i in arr:
    print(i, end="")
