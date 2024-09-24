N = int(input())
member = []
for i in range(N):
    age, name = map(str,input().split())
    temp =[int(age), name, i]
    member.append(temp)
member.sort(key = lambda x:(x[0],x[2]))
for m in member:
    print(m[0], m[1], end=" ")
    print()

# int(age) 안하고 정렬했더니 틀렸댄다. str이랑 대소비교 방법이 다른가?
# key에 lambda함수 x을 설정하고, ()