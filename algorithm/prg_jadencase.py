'''
공백이 여러 개일 수 있음
'''
def solution(s):
    s = " " + s
    ans = ""
    for i in range(1, len(s)):
        if s[i-1] == ' ':
            ans += s[i].upper()
        else:
            ans += s[i].lower()
    return ans

if __name__ == '__main__':
    print(solution(input()))