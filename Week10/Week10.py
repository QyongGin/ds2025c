# Week10

# 2025-05-12 Chapter13-2 이진 트리

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
        print(node.data, end = "->")

def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:
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
    return root # 되돌아가기

if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    # numbers = [10,15,8,3,9,1,7,100]
    root = None

    # 1
    for number in numbers:
        root = insert(root, number)

def search(target):
    current = root
    while True:
        if target == current.data:
            print(f"{target}을(를) 찾았습니다")
            break
        elif target < current.data:
            if current.left is None:
                print(f"{target}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{target}이(가) 존재하지 않습니다")
                break
            current = current.right

print("BST 구성 완료.")
post_order(root) # 3-9-8-15-10

target_num = int(input("찾는 값 입력 : "))
search(target_num)


# find_number = int(input())
# current = root
# while True:
#         if find_number == current.data:
#             print(f"{find_number}을(를) 찾았습니다")
#             break
#         elif find_number < current.data:
#             if current.left is None:
#                 print(f"{find_number}이(가) 존재하지 않습니다")
#                 break
#             current = current.left
#         else:
#             if current.right is None:
#                 print(f"{find_number}이(가) 존재하지 않습니다")
#                 break
#             current = current.right
