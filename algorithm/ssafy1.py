def main():
    T = int(input())
    for i in range(T):
        N, D, X = map(int, input().split())
        arr = list(map(int, input().split()))
        r = X - D
        if r < 0:
            r+=N
        q = arr[D-1]
        ans = N*q + r
        print('#'+str(i+1)+' '+str(ans))
            
        
if __name__ == "__main__":
    main()