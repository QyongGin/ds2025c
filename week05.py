## 2025-04-07 week05
# Chapter 10 스택

# 오퍼레이션(핵심2) : 푸시 : 집어넣다 , 팝 : 꺼내다
# 스택 : 후입선출구조, FILO, 마지막이 가장 먼저 나온다. first in last out
# 장점 : 데이터 삽입 삭제 0(1) 빠름. 단점 : 접근, 탐색 비효율
# 전역변수 : 프로그램 시작부터 끝까지 메모리 차지

# class Stack: # Stack 클래스를 만들고 배열 사용.
#     def __init__(self):
#         self.items = list()
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def size(self):
#         return len(self.items)
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def peek(self):
#         return self.items[-1] # list 맨끝
#
#
# s1 = Stack()
# s2 = Stack()
# print(s1.is_empty()) # True
# s1.push("Data structure")
# print(s1.is_empty()) # false
# print(s2.is_empty()) # True
# s1.push("Database")
# print(s1.size()) # 2
# print(s1.peek()) # Database
# print(s1.size()) # 2
# print(s1.pop()) # db remove return "Database"
# print(s1.size()) # 1
# print(s1.peek()) # Data structure

# class Node: # 링크드 리스트 활용.
#     def __init__(self, data):
#         self.data = data
#         self.link = None
#
#
# class Stack:
#     def __init__(self):
#         self.top = None # head x top
#
#     def push(self, data):
#         node = Node(data)
#         if self.top is None:
#             self.top = node
#         else:
#             node.link = self.top
#             self.top = node  # top update
#
#     def pop(self):
#         if self.top is None:
#             return "Stack is empty!"
#         popped_node = self.top # 백업용 변수 popped_node 함수가 끝나면 지역변수니까 삭제된다.
#         self.top = self.top.link # self.top이 가리켰던 노드의 link를 참조했다.
#         popped_node.link = None  # 삭제할 노드의 link까지 깔끔하게 삭제
#         return popped_node.data # 삭제하는 노드 데이터 반환.
#
#
# s1 = Stack()
# print(s1.pop())
# s1.push("Data structure")
# s1.push("Database")
# print(s1.pop())
# print(s1.pop())

s1 = list()
print(len(s1))
s1.append("Data structure") # push
s1.append("Database")
print(len(s1)) # size
print(s1[-1]) # peek
print(s1)
print(s1.pop())
print(s1)
print(s1.pop())
print(s1)
