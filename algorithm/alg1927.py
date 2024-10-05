from collections import deque

class Node:
    def __init__(self):
        self.num = 0
        self.left = None    # Node으로 초기화
        self.right = None
    def __init__(self, num):
        self.num = num
        self.left = None    # Node으로 초기화
        self.right = None
    def set_left(self, x):
        self.left = x

    def set_right(self, x):
        self.right = x

class Tree:

    def __init__(self):
        self.root = Node(0)

    def insert(self, x):
        self.current_node = self.root

        if self.current_node == None:
            self.current_node = Node(x)

        while True:
            if x < self.current_node.num:
                if self.current_node.left!= None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(x)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(x)
                    break
            
    def pop(self):
        if self.root is None:
            print(0)
        else:
            self.root, min_value = self.remove_min(self.root)
            print(min_value)

    def remove_min(self, node):
        if node.left is None:
            return node.right, node.num
        else:
            node.left, min_value = self.remove_min(node.left)
            return node, min_value


N = int(input())
tree = Tree()
for _ in range(N):
    c = int(input())
    if c != 0:
        if tree.root == None:
            tree.root = Node(c)
        else:
            tree.insert(c)
    else:
        tree.pop()


