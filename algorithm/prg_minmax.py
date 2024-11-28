def solution(s):
    arr = list(map(int, s.split()))
    answer = ''
    answer += str(min(arr))+' '+str(max(arr))
    return answer

if __name__ == '__main__':
    print(solution(input()))

