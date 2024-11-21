inputString = input()
자릿수 = len(inputString)
N = int(inputString)
sum = 0
for 자리 in range(1, 자릿수+1):
    if 자리 == 자릿수 :
        sum += 자리 * (N - 10**(자리-1) + 1)
    else :
        sum += 자리 * ((10**자리) - 1 - (10**(자리-1)) + 1)
print(sum)