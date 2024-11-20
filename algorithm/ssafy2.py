from collections import deque

def comp(arr1, arr2, k):
    maxVal = 0
    for i in range(k):
        same = 0
        for j in range(len(arr1)):
            if arr1[j] == arr2[j+i]:
                same += 1
            
        maxVal = max(same, maxVal)
    return maxVal

def main():
    T = int(input())
    for i in range(T):
        N = int(input())
        arr1 = deque(map(int, input().split()))
        arr2 = deque(map(int, input().split()))
        maxVal = 0
        maxVal = max(maxVal, comp(arr1, arr2, 1))
        for j in range(N):
            arr1.popleft()
            maxVal = max(maxVal, comp(arr1, arr2, j))
        print('#'+str(i+1)+' '+str(maxVal))
            
        
if __name__ == "__main__":
    main()