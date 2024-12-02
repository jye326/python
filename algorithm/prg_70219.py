def solution(s):
    count = 0
    count_removed_0 = 0
    while(s != '1'):
        temp = ""
        for c in s:
            if c == '0':
                count_removed_0 += 1
            else:
                temp += c
        s = format(len(temp), 'b')
        count +=1
    answer = [count, count_removed_0]
    return answer

'''
format(숫자, 'b')로 이진수 변환이 가능하다.
'''
if __name__ == '__main__':
    print(solution(input()))