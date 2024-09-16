n = int(input())
# 딕셔너리를 이용해서 간단하게 트리를 구현할 수 있다?!
tree = {}
for i in range(n):
    temp = list(input().split())
    tree[temp[0]] = [temp[1], temp[2]]
    # 간단하게 입력하는 방법이 없을까

def preorder(x):
    if x=='.':
        return
    print(x, end="")
    preorder(tree[x][0])
    preorder(tree[x][1])

def inorder(x):
    if x=='.':
        return
    inorder(tree[x][0])
    print(x, end="")
    inorder(tree[x][1])
    
def postorder(x):
    if x=='.':
        return
    postorder(tree[x][0])
    postorder(tree[x][1])
    print(x, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')