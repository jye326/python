def cal(strNum):
    mul = 1
    for c in strNum:
        mul *= int(c)
    return str(mul)

while True:
    N = input()
    if N == '0':
        break
    while len(N)>1 :
        print(N, end=" ")
        N = cal(N)
    print(N)
        


