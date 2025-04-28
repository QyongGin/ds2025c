# 2025-04-28 Chapter13 이진 트리

# 이진 탐색 트리

class TreeNode:
     def __init__(self):
         self.left = None
         self.data = None
         self.right = None

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end = "-")

if __name__ == "__main__":
    numbers = [10,15,8,3,9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

    # 2번째 원소부터
    for number in numbers[1:]:
        node = TreeNode()
        node.data = number
        current = root # 항상 첫 노드부터 비교
        while True:
            if number < current.data:
                if current.left is None: # 작은수 left
                    current.left = node
                    break
                current = current.left

            else:
                if current.right is None: # 큰수 right
                    current.right = node
                    break
                current = current.right

print("BST 구성 완료.")
post_order(root)