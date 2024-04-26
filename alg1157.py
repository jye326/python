line = input().lower()
alp = list(range(26))
for i in range(26):
    alp[i] = 0
for i in range(len(line)):
    alp[ord(line[i]) - ord('a')] += 1
if alp.count(max(alp)) == 1:
    print(chr(ord('a')+alp.index(max(alp))).upper())
else:
    print('?')