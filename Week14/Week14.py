# 소수 구하기 2초 제한

# 시간이 너무 오래 걸림.
# def is_prime(n) -> bool:
#   if n <= 1:
#       return False
#   else:
#     for i in range(2, n):
#         if n % i == 0:
#           return False
#   return True
#
# s, e = map(int, input().split())
# for i in range(s, e+1):
#   if is_prime(i):
#     print(i)

# import math
#
# def is_prime(n) -> bool:
#   if n <= 1:
#       return False
#   elif n == 2:
#       return True
#   elif n % 2 == 0:
#       return False
#   else:
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#           return False
#   return True
#
# s, e = map(int, input().split())
# for i in range(s, e+1):
#   if is_prime(i):
#     print(i)

# 스택

# import sys
# n = int(input())  # N (명령어 개수)
# stack = []  # 파이썬의 리스트를 이용
#
# for i in range(n):
#   # order = input().strip()
#   order = sys.stdin.readline().strip()
#   if 'push' in order:  # push X: 정수 X를 스택에 넣는 연산이다.
#     number = order.split()  # ex) "push 1"  --> ["push", "1"]
#     stack.append(number[-1])  # "1"
#   elif order == 'pop':  # pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#     if len(stack) == 0:  # 스택이 비어 있으면
#       print(-1)
#     else:
#       print(stack.pop())  # 출력 및 삭제. Last In First Out
#   elif order == 'size':  # size: 스택에 들어있는 정수의 개수를 출력한다.
#     print(len(stack))
#   elif order == 'empty':  # empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
#     if len(stack) == 0:  # 스택이 비어 있으면
#       print(1)
#     else:
#       print(0)
#   elif order == 'top':  # top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다. peek
#     if len(stack) == 0:  # 스택이 비어 있으면
#       print(-1)
#     else:
#       print(stack[-1])  # Top 값 출력


# 이진 탐색 노드

import sys
#sys.setrecursionlimit(10**6)

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(node, key):  # 재귀 -> 반복
  new_node = TreeNode(key)
  if root is None:
    return new_node

  current = root
  while True:
    if key < current.val:  # 현재 노드 보다 새 노드 값이 작으면
      if current.left is None:  # 현재 노드의 왼쪽이 비어있으면
        current.left = new_node
        break
      current = current.left  # 왼쪽 노드로 current 변경 (이동)
    else:  # 현재 노드 보다 새 노드 값이 크면
      if current.right is None:  # 현재 노드의 오른쪽이 비어있으면
        current.right = new_node  # 새 노드 연결
        break
      current = current.right  # 오른쪽 노드로 current 변경 (이동)
  return root


def post_order(node):  # 재귀 -> 반복
  if node is None:
    return

  stack = list()
  output = list()
  stack.append(node)

  while stack:
    current = stack.pop()
    output.append(current.val)

    if current.left:
      stack.append(current.left)  # push
    if current.right:
      stack.append(current.right)  # push

  for value in reversed(output):
    print(value)


inputs = [50, 30, 24, 5, 28, 45, 98, 52, 60]  # preorder input
root = None
# for i in sys.stdin:
#   root = insert(root, int(i.strip()))
for i in inputs:
   root = insert(root, i)

post_order(root)