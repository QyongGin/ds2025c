# 2025-04-28 Chapter13 이진 트리


# pre order 전위 PLR <처리 -> left -> right> hs - sl - hw - zz - mb - sm

def pre_order(node):
    if node:
        print(node.data, end='-')
        pre_order(node.left)
        pre_order(node.right)

# In order 중위 LPR -> hw - sl - zz -hs - sm

def in_order(node):
    if node:
        in_order(node.left)
        print(node.data, end='-')
        in_order(node.right)


# Post order 후위 LRP Left Right Process(처리) 1. hw return node2 right -> node5 zz
# -> Left부터 시행 Left null 이거나 시행했다면 right 반복. 둘 다 불가능하다면 Process 출력.
def post_order(node):
    if node:
         post_order(node.left) # node2 left -> node4.left -> none -> node4.right -> none -> hw -> node2.right
         post_order(node.right)
         print(node.data, end='-')


class TreeNode:
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None



node1 = TreeNode()
node1.data = "hs"

node2 = TreeNode()
node2.data = 'sl'
node1.left = node2

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

post_order(node1)
print()
in_order(node1)
print()
pre_order(node1)