def solution(A,B):
    answer = 0
    '''
    A의 최댓값 * B의 최솟값으로 가야돼.
    '''
    A.sort()
    B.sort()
    for i in range(len(A)):
        answer += A[i]*B[len(B)-1-i]
    return answer