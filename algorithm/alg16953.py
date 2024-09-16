A, B = map(int, input().split())
count= 0
while(B>A):
    count+=1
    if(B%10==1):
        #10곱하고 더하기 1한 것
        B-=1
        B/=10
    else:
        #2곱한 것
        B/=2
if(A==B):
    print(count+1)
else:
    print(-1)