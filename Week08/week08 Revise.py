# 이진 탐색 트리

class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None

def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:
        return new_node

    current = root

    while True:
        if value < current.data:
            if current.left is None: # 현재 값의 left가 None이라면 newnode를 추가하고 종료.
                current.left = new_node
                break
            current = current.left # 현재 값의 left에 이미 노드가 있다면 그 노드를 현재값으로 바꾸고 반복문 재시행.
        else:
            if current.right is None:
                current.right = new_node
                break
            current = current.right # move
    return root # 만약 root가 None이 아닐 경우에는 root가 다시 초기화되니 저장했던 root값 반환.

if __name__ == "__main__":
# __name__ == 직접 실행하면 "__main__"이 되고 import되면 "파일이름"이 된다.
# import는 다른 파일에서 나를 import 부를 때. 지금은 이 파일이 직접 실행된 경우에만 아래 코드 실행하라는 말.
    numbers = [10,15,8,3,9] # 추가할 노드 목록
    root = None

    for number in numbers:
        root = insert(root,number)

