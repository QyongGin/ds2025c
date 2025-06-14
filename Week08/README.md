# Chapter13 이진 트리
### 트리
- 노드를 연결해 계층 구조를 만드는 비선형 추상 데이터 타입.
- 기본 동작에는 삽입과 탐색, 삭제.
<img width="352" alt="image" src="https://github.com/user-attachments/assets/1c74ce4d-c890-4ac9-9b37-3e65cba8ef92" />

### 일반 트리 
- 맨 위 하나의 노드를 두고 시작하는 자료 구조.
- 루트 노드(Root Node) : 트리의 맨 위 노드, 루트 노드를 제외한 모든 노드는 부모 노드가 있다.
- 자식 노드(Child Node) : 노드의 아래로 연결된 링크드 노드
- 부모 노드(Parent Node) : 하나 이상의 자식 노드를 보유
- 형제 노드(Sibling Node) : 같은 부모 노드를 공유
- 에지(Edge) : 트리에서 두 노드 사이의 연결
- 리프 노드(Leaf Node) : 자식 노드가 없는 노드
- 브랜치 노드(Branch Node) : 자식 노드가 있는 노드
- 자손 : 노드의 자식과 그 자식, 그 자식의 자식 노드 모두를 이르는 말
- 서브트리 : 루트 노드를 제외한 노드와 그 자손 노드 
<img width="307" alt="image" src="https://github.com/user-attachments/assets/db4e3ae8-22ef-47a2-a3ff-18c76789a1ea" />

### 이진 트리(Binary Tree)
- 각각의 노드가 최대 두 개의 자식 노드만 가질 수 잇는 트리 자료구조
- 모든 노드는 루트 노드를 제외하고 부모 노드의 왼쪽 또는 오른쪽 자식 노드다.
- 이진 트리와 일반 트리의 유일한 차이는 자식 노드의 제한.
<img width="278" alt="image" src="https://github.com/user-attachments/assets/58f23da4-92b4-4a1c-89e4-b5717db09ebf" />

### 이진 탐색 트리(Binary Search Tree)
- 각각의 노드가 최대 두 개의 자식만 가진다.
- 각 노드의 값이 왼쪽 서브트리의 어떠한 값보다 크고, 오른쪽 서브트리에 있는 어떤 값보다 작도록 정렬, 저장하는 트리 자료구조.
- 중복 값을 저장하지 못한다.
<img width="267" alt="image" src="https://github.com/user-attachments/assets/ad6bd3da-237d-452e-acc3-c9d7cdc226e6" />

- 트리 전체를 이동하려면 백트래킹이 필요한 경우가 많다. 루트 노드에서 시작해 어떤 노드로든 이동할 수 있지만, 루트 노트에서 벗어나면
  그 노드의 하위 노드로만 이동할 수 있다.
<img width="302" alt="image" src="https://github.com/user-attachments/assets/2a939b23-8e76-471a-a5fc-4c53e97e22e8" />

- 오른쪽 자식 노드로만 이동하면 A, C, E 순서로 이동한다. 이 경우, C 노드로 백트래킹 하지 않으면 노드 D에 도달하지 못한다.

### 트리를 사용해야 할 때
- 일반 트리와 이진 트리에서 데이터의 삽입, 삭제, 탐색 작업은 모두 0(n) 선형시간을 따른다.
- 이진 탐색 트리는 데이터의 접근, 탐색, 삽입, 삭제에 이진 탐색을 사용하기에 O(log n) 로그 함수를 따른다.
<img width="582" alt="image" src="https://github.com/user-attachments/assets/861c7e83-8e3b-44c9-944f-993b1d385e1a" />

- 트리는 선형 자료구조로 표현하기 어렵거나 불가능한 계층적 정보를 저장한다.
<img width="549" alt="image" src="https://github.com/user-attachments/assets/147db9ea-7ac8-4cc2-af25-a7587a6693da" />

- HTML과 XML 문서도 트리로 표현 가능한 데이터 계층 구조이다.
    - HTML은 웹 페이지를 만들 때 사용하는 마크업 언어
    - XML은 문서를 만들 때 사용하는 마크업 언어
- 보통 HTML과 XML은 태그를 중첩할 수 있어 트리로 표현하며, 각 노드는 HTML이나 XML의 요소를 나타낸다.
- 문서 객체 모델(DOM Document Object Model) : XML이나 HTML 문서를 트리로 나타내는 언어 독립적 인터페이스. JS가 사용.
<img width="443" alt="image" src="https://github.com/user-attachments/assets/020ace5b-03c4-4f05-b474-33f4bf38fc1a" />

- 산술 표현식 역시 트리 형태로 분석 가능하다.
- 2 + 3 * 4를 예로 든다. 트리 아래로 곱셈을 내리고 3 * 4를 계산 후 2 + 12를 계산해 답을 얻는다. 이런 트리가 파스 트리다.
- 파스 트리(Parse Tree) : 표현식 평가 규칙과 같은 일정한 문법에 따라 데이터를 저장하는 정렬된 트리.
<img width="186" alt="image" src="https://github.com/user-attachments/assets/75d37b12-18b4-4533-a77f-1b15d663ffb7" />

### 이진 탐색의 장점
- 해시 테이블은 충돌로 인해 실제 저장하는 데이터보다 열 배 이상의 공간을 사용한다. 데이터를 순서대로 저장하지 않아, 순서에 따라 이동하지 못한다.
- 반면, 이진 탐색 트리는 메모리를 낭비하지 않는다. 데이터의 정렬된 순서나 역순으로 빠르게 이동 가능하다.

# 트리 만들기

### 트리의 구조 예시
```python
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

print(node5.data)
print(node1.left.right.data) # node1.left->node2.right->node5 'zz'
```
<img width="444" alt="image" src="https://github.com/user-attachments/assets/046fdb22-dbef-46c7-b694-2e0635162a95" />

### 삽입 insert

```python
def insert(root, value):
    new_node = TreeNode()
    new_node.data = value

    if root is None:   # 루트 노드가 없다면 반환해서 루트 노드로 저장.
        return new_node

    current = root  # 항상 첫 노드부터 비교, 처음 반환했던 루트 활용.
    while True:
        if value < current.data: # 루트노드보다 작다면 left
            if current.left is None:  # left가 비었다면 삽입
                current.left = new_node
                break
            current = current.left # 이미 있다면 left로 move 후 재비교.

        else:  # 루트노드보다 크다면 right
            if current.right is None:  
                current.right = new_node
                break
            current = current.right # 이미 있다면 right move 후 재비교
    return root # 루트 노드 반환하지 않으면 계속 초기화된다., 처음 썻던 루트노드 10 반환해서 계속 재사용 

if __name__ == "__main__":   # !! 프로그램 직접 실행 시 자동 수행.
    numbers = [10, 15, 8, 3, 9]
    root = None

    for number in numbers:
        root = insert(root, number) # 마지막에 루트노드 '10' 반환 전역변수 root로 재사용
```

### 탐색 search

```python
def search():
    target = int(input())
    current = root

    while True:
        if target == current.data:
            print(f"{target}을 찾았습니다.")
            break
        elif target < current.data: 
            if current.left is None:
                print(f"{target}을 못 찾았습니다.")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{target}을 못 찾았습니다.")
                break
            current = current.right

search()
# 입력 부분을 search에서 제거하거나 print문을 빼오고 return boolen값을 추가해서 만들 수도 있다.
```

### 삭제 delete

```python
# numbers = [10, 15, 8, 3, 9, 14]
def delete(node,value):
    if node is None:
        print(f"트리가 없습니다.")
        return None

    if value < node.data:
        node.left = delete(node.left,value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else: # 삭제할 노드 발견
          # 자식 노드가 1개거나 leaf노드인 경우 (없는)
        if node.left is None: # 왼쪽 자식이 없다면
            return node.right # 오른쪽 자식 노드랑 남은 노드랑 이어주기
        elif node.right is None: # 반대로 반복
            return node.left
        
    return root
```
<img width="510" alt="image" src="https://github.com/user-attachments/assets/06e626e9-9cd9-4e0e-af14-d4c0c9bf9a01" />

- ``delete(root,15)``를 실행한다면 right 자식 노드가 None이니 남은 left 노드 14를 남은 노드와 연결시켜 준다.

<img width="510" alt="image" src="https://github.com/user-attachments/assets/2e33e2f5-8ca0-4601-ac1c-668a0da8b30c" />

### 삭제 delete (자식 노드가 left right 둘 다 있는 경우)
- 방법은 두 가지가 있다.
1. 오른쪽 서브트리에서 가장 작은 값 (Successor) (실전에서 더 자주 사용)
   - 삭제할 값보다 크면서 가장 작은 값
   - 항상 node.right 쪽의 제일 왼쪽 값
   - 구현이 직관적이고 간단하다.
   - 지워질 노드 대신 다음 값을 올린다는 흐름에 더 직관적이다. 
     
2. 왼쪽 서브트리에서 가장 큰 값 (Predecessor)
   - 삭제할 값보다 작으면서 가장 큰 값
   - node.left 쪽의 제일 오른쪽 값

```python
# 자식 노드가 2개인 경우
# Successor(후임자, 해당 노드보다 값이 큰 노드 중 가장 작은 값)  사용. 
        min_larger_node = node.right # right 서브트리에서 가장 작은 값  
        while min_larger_node.left:
            min_larger_node = min_larger_node.left  # move
        node.data = min_larger_node.data  # 삭제 노드의 데이터에 Successor 데이터 덧씌우기 
        node.right = delete(node.right, min_larger_node.data) # 기존 Successor 삭제 
    return node
```

# 너비 우선 탐색 Breadth-First Search
- 너비 우선 이동은 '레벨'의 순서대로 모든 노드에 방문한다. 루트 노드가 레벨 0 자식 레벨 1 손자 레벨 2
- 너비 우선 이동을 사용해 데이터를 탐색할 때, 이를 너비 우선 탐색 Breadth-First Search라고 한다.
- 마지막 레벨 도달전까지 반복. 현재 레벨과 다음 레벨 저장하는 각각의 리스트 활용.

```python
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
    return False # 다음 노드가 없다면 찾지 못했다는 뜻. False

target = int(input("찾을 노드 : "))
breadth_first_search(root,target)
if target:
    print("찾음")
else:
    print("없음")
```
<img width="510" alt="image" src="https://github.com/user-attachments/assets/d83eee6a-faa6-4a70-ba6e-5b4ec7458cf1" />


# 깊이 우선 이동 Depth-First Traversal
- 이진 트리의 모든 노드를 한 방향으로 방문하고 다음 형제 노드로 이동한다.
- 깊이 우선 이동은 다시 전위 Pre order, 후위 Post order, 중위 In order로 나뉜다.
- 깊이 우선 이동을 사용해 데이터를 탐색하면 이를 깊이 우선 탐색 Depth-First Search

### 전위 이동 Pre order
- 전위 이동은 루트 노드에서 시작해 왼쪽으로 이동하고 오른쪽 서브트리로 이동한다.
```python
def pre_order(node): # 명확하게 명시하는 방법
  if node is None: # None이다 => 자식 노드가 없다. => 백트래킹
    return         
  print(node.data, end = '-') # 루트 노드 출력
  pre_order(node.left)  # 왼쪽 자식 노드가 None이 아니라면 계속 이동. 백트래킹 됐다면 다음 코드로 이동. 
  pre_order(node.right) # 오른쪽 자식 노드로 계속 이동. 백트래킹 됐다면 다음 코드로 이동.
  # 끝나면 불러온 노드로 돌아가 다시 코드 시행.
```
<img width="510" alt="image" src="https://github.com/user-attachments/assets/dc634c16-4cbb-40b2-b2fe-bd136f254a22" />

### 후위 이동 Post order
- 후위 이동은 트리의 왼쪽에서 시작해 오른쪽 서브트리로 이동한 다음 루트노드에서 끝난다.
```python
# 왼쪽과 오른쪽 자식 노드 이동. 자식노드 모두 None이라면 print 후 백트래킹 

def post_order(node):
  if node: # 더 간결한 코드 
    post_order(node.left)
    post_order(node.right)
    print(node.data, end = '-')
```
<img width="510" alt="image" src="https://github.com/user-attachments/assets/2ac14a48-e2a0-4316-9783-1c3c7c97a76e" />

### 중위 이동 In order
- 노드의 값을 출력하는 작업을 두 가지 재귀 호출의 '중간'에 수행한다.
- 중위 이동은 트리의 왼쪽에서 시작해 루트 노드로 이동 후 다음 오른쪽 서브트리로 이동한다.
```python
def in_order(node):
  if node:
    in_order(node.left)
    print(node.data, end = '-')
    in_order(node.right)
```
<img width="510" alt="image" src="https://github.com/user-attachments/assets/938914ab-4859-4f7a-b248-f6edfe4ebeb0" />

### __name__ 이란? 
- 파일이 직접 실행되면 ``__name__``의 값은 ``__main__``이 된다.
- 다른 파일에 의해 ``import`` 된다면 ``__name__``은 그 파일의 모듈 이름이 된다.
- ``if __name__ == "__main__"`` 이 파일이 직접 실행됐을 때만 아래 코드를 실행한다.

```python
class TreeNode:
     def __init__(self):
         self.left = None
         self.data = None
         self.right = None

if __name__ == "__main__": 
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

    # 2번째 원소 부터 마지막 원소까지
    for number in numbers[1:]:
        node = TreeNode()
        node.data = number
        current = root
        while True:      # 루트 노드보다 작은 노드는 left, 큰 노드는 right로 정렬.
            if number < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # 루트 노드.left에 노드가 있다면 current move
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move

    print("BST 구성 완료") # 이진 탐색 트리 Binary Search Tree
```
 <img width="510" alt="image" src="https://github.com/user-attachments/assets/07156047-3b1d-4716-aa06-a3cc531b637d" />

## 이진 트리 뒤집기
### 이진 트리 반전 Inverting a binary tree 
- 모든 노드를 서로 바꾼다. right 노드는 전부 left 노드. left 노드는 모두 right 노드가 된다.
- 이진 트리를 뒤집기 위해 모든 노드를 방문하며 각 노드의 자식을 추적해야 한다.
  - 너비 우선 탐색을 사용해 왼쪽과 오른쪽 자식을 각각 추적해 뒤집는다.

```python 
def invert(root):
    current = [root] # 너비 우선 탐색 이용
    next = []
    while current:
        for node in current: # 현재 노드 리스트에서 node get
            if node.left:
                next.append(node.left)
            if node.right:
                next.append(node.right)
            tmp = node.left # tmp 임시변수
            node.left = node.right # left에 right 덧씌우기, data만 바꾼게 아니라 노드 자체를 바꿨기에 자식 노드도 따라간다.
            node.right = tmp # 임시저장한 left 덧씌우기
        current = next #
        next = []


# root는 객체일 뿐. root 자체만으로 자식 노드 모두 선택하지 못한다
post_order(root) # 3->9->8->14->10->
invert(root) 
print()
post_order(root) # 14->9->3->8->10->
```

<img width="626" alt="image" src="https://github.com/user-attachments/assets/3a47b1af-8122-4e72-af57-b7c33e498021" />

- 노드를 덧씌울 때, 서브 트리 자체가 옮겨진다고 생각하면 편하다.
- 8과 14는 각각 left, right 서브트리였지만 14는 left 서브트리가 되고 8과 그에 묶인 9,3까지 통째로 right 서브트리로
  옮겨진다.

### 깊이 우선 탐색으로 이진 트리 뒤집기
```python
def invert_dfs(node):
    if node:
        # 구조를 바꾸는 건 자기 자신을 재귀적으로 호출해야 한다.
        # 왼쪽 서브 트리부터 왼쪽으로 끝까지 이동하고 오른쪽 자식 노드까지 이동.
        # 리프 노드는 None끼리 swap하고 동작이 끝난다. 부모 노드가 그 자식 노드를 서로 swap시킨다.
        # -> 자식 노드부터 반전시키고 부모 노드 반전.

        invert_dfs(node.left)
        invert_dfs(node.right)

        node.left, node.right = node.right, node.left # 자식이 한 쪽만 있어도 swap 필요
        
    # if node: post_order로 부르는건 출력할 뿐이지 구조를 바꾸는게 아니다. 불가능.
    #     post_order(node.left)
    #     post_order(node.right)
    #     if node.left and node.right:
    #         tmp = node.left
    #         node.left = node.right
    #         node.right = tmp
```
### 재귀함수 recursive function
- 자기 자신을 다시 호출하는 함수
- 2가지 핵심 구성 요소
  - Base Case (종료 조건) : 더 이상 재귀 호출을 하지 않고 종료하는 조건
  - Recursive Case (자기 자신 호출) : 문제를 더 작은 문제로 바꿔 자기 자신을 다시 호출
- 트리 탐색(전위, 중위, 후위)가 대표적인 예.
- 반복 가능한 문제를 더 작게 쪼개어 해결할 때 유용하다.



