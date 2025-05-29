#def pre_order(node): # 전위탐색, 방문순서 : 루트,왼쪽 서브트리,오른쪽 서브트리

def pre_order(node): # 전위 이동
    if node is None:
        return
    print(node.data, end='-')
    pre_order(node.left)
    pre_order(node.right)
    # if node:
    #     print(node.data, end='-')
    #     pre_order(node.left)
    #     pre_order(node.right)


def in_order(node):
    # if node is None:
    #     return
    # in_order(node.left)
    # print(node.data, end='-')
    # in_order(node.right)
    if node:
        in_order(node.left)
        print(node.data, end='-')
        in_order(node.right)


def post_order(node):
    # if node is None:
    #     return
    # post_order(node.left)
    # post_order(node.right)
    # print(node.data, end='-')
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end='-')

class TreeNode: # 노드 생성, 초기화
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

node1 = TreeNode()
node1.data = 'hs'

node2 = TreeNode()
node2.data = 'sl'
node1.left = node2 # node1의 왼쪽 자식 노드에 node2 추가

node3 = TreeNode()
node3.data = 'mb'
node1.right = node3

node4 = TreeNode()
node4.data = 'hw'
node2.left = node4

node5 = TreeNode()
node5.data = 'zz'
node2.right = node5

node6 = TreeNode()
node6.data = 'sm'
node3.left = node6

print(in_order(node1))
