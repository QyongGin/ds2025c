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
        print(node.data, end = "->")

def pre_order(node): # 명확하게 명시하는 방법
  if node is None: # None이다 => 자식 노드가 없다. => 백트래킹
    return
  print(node.data, end = '-') # 루트 노드 출력
  pre_order(node.left)  # 왼쪽 자식 노드가 None이 아니라면 계속 이동. 백트래킹 됐다면 다음 코드로 이동.
  pre_order(node.right) # 오른쪽 자식 노드로 계속 이동. 백트래킹 됐다면 다음 코드로 이동.

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
    return root

# __name__ == "__main__" 프로그램을 내가 직접 실행했다면
# 삽입할 데이터 목록을 배열로 선언하고 root를 None으로 미리 선언한다.
# numbers를 for문으로 요소를 하나씩 가져와 insert 메소드에 대입시켜서 root에 저장시킨다.
if __name__ == "__main__":
    numbers = [10, 8, 3, 9, 14] # 넣을 데이터 목록
    root = None

    # 1
    for number in numbers:
        root = insert(root, number) # insert를 실행하고 root를 받는다.

# 검색 메소드
# 현재 노드의 값과 찾으려는 값을 비교한다.
# 현재 노드보다 작으면 left 이동, 크면 right 이동
# 더 이상 이동할 노드가 없다면 break, 찾지 못함.
def search(target):
    current = root

    while True:
        if target == current.data:
            print(f"{target}을 찾았습니다.")
            break
        elif target < current.data: # 현재 값보다 작다면 왼쪽으로 이동
            if current.left is None: # 이동하려는데 왼쪽 자식노드가 없다면? 더 이상 이동할 노드가 없다.
                print(f"{target}을 못 찾았습니다.")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{target}을 못 찾았습니다.")
                break
            current = current.right

# 삭제 메소드
#
def delete(node,value):
    if node is None: # 시작할 노드가 없다면
        print(f"트리가 없습니다.")
        return None

    if value < node.data: # value가 현재 노드 값보다 작다면 왼쪽 자식 노드를 매개변수로 재귀 함수 호출
        node.left = delete(node.left,value) # 재귀 함수 사용 - 함수에서 자기 자신을 호출해서 작업 수행
    elif value > node.data:
        node.right = delete(node.right, value)
    else: # 삭제할 노드 발견
        # 노드를 삭제하면 그 노드의 부모와 자식 노드를 연결할 노드가 비게 된다.
        # 삭제될 노드의 뒤를 이을 왼쪽 자식 노드가 없다면
        if node.left is None:
            return node.right # 오른쪽 자식 노드랑 남은 노드랑 이어주기
        elif node.right is None: # 반대로 반복
            return node.left
        # 자식이 둘 다 존재한다. -> 누구랑 연결시키지? -> 삭제될 노드의 오른쪽 자식 노드 중에서 가장 작은 값을 연결시킨다.
        else:
            current = node.right  # 현재 노드를 노드의 오른쪽 자식으로 선언
            while True:
                if current.left is None: # 왼쪽 자식이 없다면 그만.
                    break
                else:
                    current = current.left # 왼쪽 자식 노드가 있다면? 이동
            return current # 삭제될 노드의 오른쪽 자식에서 가장 작은 노드를 반환, 연결.

    return node

def breadth_first_search(root,target):
    current = [root] # 순회가능케 리스트로 선언. = root는 순회 불가능
    next = [] # 다음 찾을 노드 리스트
    while current:
        for node in current:
            if node.data == target:
                return True
            # left 노드, right 노드 자식이 있다면 next 리스트에 추가
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
        current = next # 현재 찾을 노드
        next = [] # 다음 찾을 노드 초기화
    return False # 다음 노드가 없다면 False

def invert(root):
    current = [root] # 너비 우선 탐색 이용
    next = []
    while current:
        for node in current:
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            tmp = node.left # tmp 임시변수
            # data를 바꾸는게 아닌, 누구를 참조하는지를 바꾸기 때문에 그들의 자식 노드도 함께 이동한다.
            node.left = node.right # left에 right 덧씌우기
            node.right = tmp # 임시저장한 left 덧씌우기
        current = next #
        next = []


def invert_dfs(node):
    if node:
        # 자기 자신을 재귀적으로 호출
        # 왼쪽 서브트리로 먼저 이동하여 좌우 자식 노드 없을 때 까지 재귀 호출.
        # -> 자식 노드 먼저 반전 시키고 부모 노드끼리 반전. -> post_order와 유사하다.
        invert_dfs(node.left)
        invert_dfs(node.right)

        # 자식이 한 쪽만 있어도 좌에서 우(None)로 가는 등, 반전 시킨다.
        node.left, node.right = node.right, node.left
    # if node:
    #     post_order(node.left)
    #     post_order(node.right)
    #     if node.left and node.right:
    #         tmp = node.left
    #         node.left = node.right
    #         node.right = tmp


post_order(root) #root는 객체일 뿐. root 자체만으로 자식 노드 모두 선택하지 못한다.
invert_dfs(root)
print()
post_order(root)




