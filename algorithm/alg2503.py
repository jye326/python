# 123 ~ 987까지의 모든 수에 대하여 다음을 만족하는 수를 정답 후보 리스트에 추가
# 1. num에 대해 strike ball 갯수가 맞는지 체크 -> 맞으면 정답 후보에 넣고
# 1. 초기에 123~987까지의 모든 수에 대하여 돌리던 것을 정답후보에 있는 애들로만 돌리기
# N회 반복

# 각 자릿수를 추출하여 리스트로 반환
def extract_digit(x):
    third = x % 10
    x = x // 10
    second = x % 10
    first = x //10
    return [first, second, third]
# target num과 some x을 list of digits형태로 입력받아 strike ball 갯수를 각각 반환
def strike_ball_check(num_list, x_list):
    strike = 0
    ball = 0
    for i in range(len(num_list)):
        if x_list[i] == num_list[i]:
            strike+=1
        elif x_list[i] in num_list:
            ball+=1
    return strike, ball

def filter_next_answer(ans, num,strike, ball):
    digits_of_num = extract_digit(num)
    new_ans = list()
    for x in ans:
        digits_of_x = extract_digit(x)
        s, b = strike_ball_check(digits_of_num, digits_of_x)
        if s==strike and b == ball:
            new_ans.append(x)
    return new_ans
# 필터링된 정답 후보리스트를 반환

N = int(input())
# ans 초기화
ans = list()
for i in range(1,10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i!=j and j!=k and i!=k:#각 자리는 겹치지 않아야 함
                ans.append(i*100 + j*10 + k)
# 리스트를 입력받아 주어진 리스트의 모든 수에 대하여 strike ball 갯수를 count하여
# 통과하는 것만 새로운 리스트에 담아 반환하는 함수
for _ in range(N):
    num, strike, ball = map(int, input().split())
    ans = filter_next_answer(ans=ans, num=num, strike=strike, ball= ball)
print(len(ans))