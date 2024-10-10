while(True):
    temp = list(map(int, input().split()))
    if temp == [0, 0, 0]:
        break
    temp.sort()
    if pow(temp[2], 2) == pow(temp[0], 2) + pow(temp[1], 2):
        print('right')
    else:
        print('wrong')


