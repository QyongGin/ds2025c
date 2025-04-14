## 2025-04-07 week05
# Chapter 10 스택
from inspect import stack


# 오퍼레이션(핵심2) : 푸시 : 집어넣다 , 팝 : 꺼내다
# 스택 : 후입 선출 자료구조, LIFO(Last in First out), 마지막이 가장 먼저 나온다.
# -> 가장 최근에 추가한 요소만 제거하는 선형 자료구조. 반드시 순서를 따라야해서 "접근이 제한된 자료구조"라고도 함.

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

# s1 = list()
# print(len(s1))
# s1.append("Data structure") # push
# s1.append("Database")
# print(len(s1)) # size
# print(s1[-1]) # peek
# print(s1)
# print(s1.pop())
# print(s1)
# print(s1.pop())
# print(s1)

def check_parentheses(expression : str) -> bool: # type hint -> parameter data type은
    # str이라는 힌트와 return type이 bool이라는 힌트를 준다.
    # 대신 강제하지 않는다.
    # 중괄호 {}의 짝도 확인하게 확장했다.
    # 허나, 지금은 ([2+1)] 도 true를 출력하게 되어서 추후 수정이 필요함. [-1]로 마지막 값을 가져와야 함.
    stack = []
    for letter in expression:
        if letter == "(":           # 사용자가 입력한 문자 확인
            stack.append(letter)
        elif letter == "{":
            stack.append(letter)

        if letter == ")":           # 괄호를 닫는 문자가 오면
            if len(stack) == 0:
                return False
            elif stack[-1] == "(":
                stack.pop()
            elif stack[-1] == "{": # {) 오류 {() ({}) 가능하게
                return False

        elif letter == "}":
            if len(stack) == 0:
                return False
            elif stack[-1] == "{":
                stack.pop()
            elif stack[-1] == "(": # (}오류 {()} ({}
                return False

    return len(stack) == 0

print(check_parentheses("({2+3})"))
print(check_parentheses("({2+3)}"))
print(check_parentheses("{)2+3(())}"))
print(check_parentheses("({2+3)"))
print(check_parentheses("{(2+(3*9))}"))
print(check_parentheses("(2+(3*9))"))
print(check_parentheses("(2+3)"))
print(check_parentheses("({2+3)}"))

# 딕셔너리 -> 키 : 여는괄호 밸류 : 닫는괄호
# brackets = { ']':'['. '}':'{' }  짝이 맞으면 넘어가고


###

# class Stack:
#     def __init__(self):  # 클래스의 인스턴스 생성시 자동 호출
#         self.items = []  # 인스턴스 변수 items 비어있는 리스트로 초기화
#
#     def push(self, data):
#         self.items.append(data)  # 배열에 매개변수 data append 추가
#
#     def pop(self):
#         return self.items.pop()  # 가장 최근 추가된 요소 삭제 후 반환.
#
#     def size(self):
#         return len(self.items)
#
#     def is_empty(self):
#         return len(self.items) == 0
#
#     def peek(self):
#         return self.items[-1]
#
# s1 = Stack()
# s1.push(1)
# print(s1.peek())  # 마지막 요소 출력
# s1.push(2)
# print(s1.peek())
# print(s1.pop())
# print(s1.peek())
# print(s1.size())
# print(s1.is_empty())

# stack = []
# print(stack)
# stack.append('용진') #
# print(stack)
# stack.append('용-진')
# print(stack[-1])
# stack.append('대상혁')
# print(len(stack))
# print(stack.pop())
# print(stack)

# def reverse_string(a_string): // 문자열 뒤집기
#     stack = []
#     string = ""
#     for c in a_string:
#         stack.append(c)  # 문자열의 문자 하나씩 stack에 추가
#     for c in a_string:
#         string += stack.pop()  # string에 stack의 마지막 요소부터 추가
#     return string
#
# print(reverse_string("Bieber"))
# -> "rebeiB

# 최소 스택
# 푸시와 팝으로 가장 작은 요소를 반환하는 메서드를 가진 자료구조 설계
# 두 개의 스택, 메인과 최소 사용. 메인이 푸시와 팝 지원, 최소는 가장 작은 요소 추적.

class MinStack():
    def __init__(self):
        self.main = []
        self.min = []

    def push(self, n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n <= self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1]) # main과 요소 수를 동일하게 유지하려고. 어차피 마지막에 main에 입력한 데이터 저장.
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]

# 최대 스택

class MaxStack():
    def __init__(self):
        self.main = []
        self.max = []

    def push(self, n):
        if len(self.main) == 0:
            self.max.append(n)
        elif n >= self.max:
            self.max.append(n)
        else:
            self.max.append(self.max[-1])
        self.main.append(n)

    def pop(self):
        self.max.pop()
        return self.main.pop

    def get_max(self):
        return self.max.peek  # 어차피 -1로 마지막 요소를 추가한다면 peek도 무관.



































