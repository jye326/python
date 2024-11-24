'''
한쪽으로만 이어 붙인다. 자꾸 양쪽을 생각하지 말자.
이 경우 dp[i] 는
dp[i-1]의 경우에서 세로로 반쪽 붙이는거랑
dp[i-2]에서 가로로 반쪽 두개 붙이거나, 네모하나 붙이는거다.
'''
arr = list(range(251))
arr[0] = 1
arr[1] = 1
arr[2] = 3
for i in range(3, 251):
    arr[i] = arr[i-1] + arr[i-2]*2
while True:
    try :
        print(arr[int(input())])
    except EOFError:
        break