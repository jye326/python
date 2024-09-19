A, B, C = map(int, input().split())

def fpow(A, B, C):#A의 B승 분할정복으로 구하기
    if B == 1:
        return A%C
    x = fpow(A, B//2, C)   # 몫은 //임
    
    if(B%2 == 0):
        return (x*x)%C
    else:
        return (x*x*A)%C

print(fpow(A,B=B,C=C))