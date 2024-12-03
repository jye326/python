def solution(n):
    answer = 0
    for i in range(1, n+1):
        answer += continuousSum(i, n)
    return answer

def continuousSum(start, n):
    sum = 0
    while sum < n:
        sum += start
        start += 1
        if sum == n:
            return 1
    return 0

if __name__ == '__main__':
    print(solution(int(input())))