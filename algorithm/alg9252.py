#문자열 자체를 리스트로 가져도 되네
import sys 
input = sys.stdin.readline
A = [""] + list(input().rstrip())
B = [""] + list(input().rstrip())
LCS = [[""]*len(B) for _ in range(len(A))]
# LCS[i][j]가 A의 i번째까지의 문자열과
# B의 j번째 까지의 문자열의 LCS
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + A[i]
        else:
            if len(LCS[i-1][j])>=len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]
result = LCS[-1][-1]
print(len(result), result, sep="\n")