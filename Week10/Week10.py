# Week10

# 2025-05-12 Chapter13-2 이진 트리

# 이진 탐색 트리
# +Delete

class TreeNode:
     def __init__(self):
         self.left = None
         self.data = None
         self.right = None

def post_order(node):
    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.data, end = "-> ")


def insert(node, value):
    new_node = TreeNode()
    new_node.data = value

    if node is None:
        return new_node

    current = root  # 항상 첫 노드부터 비교
    while True:
        if value < current.data:
            if current.left is None:  # 작은수 left
                current.left = new_node
                break
            current = current.left

        else:
            if current.right is None:  # 큰수 right
                current.right = new_node
                break
            current = current.right # move
    return node # 되돌아가기

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9, 14]
    # numbers = [10,15,8,3,9,1,7,100]
    root = None

    # 1
    for number in numbers:
        root = insert(root, number)

def search(target):
    current = root
    while True:
        if target == current.data:
            return True
        elif target < current.data:
            if current.left is None:
                return False
            current = current.left
        else:
            if current.right is None:
                return False
            current = current.right

def delete(node, value):
    if node is None:
        return None

    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else: # 삭제할 노드 발견
        # 자식 노드가 1개 이거나 leaf노드인 경우
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # 자식 노드가 2개인 경우
        # min_larger_node = node.right
        # while min_larger_node.left:
        #     min_larger_node = min_larger_node.left
        # node.data = min_larger_node.data
        # node.right = delete(node.right, min_larger_node.data)

        max_minimul_node = node.left
        while max_minimul_node.right:
            max_minimul_node = max_minimul_node.right
        node.data = max_minimul_node.data
        node.left = delete(node.left, max_minimul_node.data)

    return node


print("BST 구성 완료.")
post_order(root) # 3-9-8-15-10

target_num = int(input("찾는 값 입력 : "))
if search(target_num):
    print(f"{target_num}을(를) 찾았습니다")
else:
    print(f"{target_num}이(가) 존재하지 않습니다")

del_num = int(input("삭제할 값 입력 : "))
root = delete(root, del_num)
post_order(root)
print()