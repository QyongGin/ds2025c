# 큐
# 선입선출
# 프론트 리어

class Node:
    def __init__(self,data, link=None):
        self.data = data
        self.link = link
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self, data):
        self.size = self.size + 1
        node = Node(data)
        if self.rear is None:
            self.front = node
            self.rear = node
        else:
            self.rear.link = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue is empty!")
        self.size = self.size - 1
        temp = self.front             # 선입 저장
        self.front = self.front.link  # 이제 선입은 다음 입력됐던 값으로
        if self.front is None:        # 다음 값이 없다면
            self.rear = None          # 마지막 값이 삭제됐으니 rear도 None 설정
        temp.link = None
        return temp.data

q = Queue()
q.enqueue("Database")
q.enqueue("Data structure")
print(q.size, q.front.data, q.rear.data)
q.dequeue()
print(q.size, q.front.data, q.rear.data)
q.dequeue()
print(q.size, q.front, q.rear) # data가 None이 됐으니 속성이 사라졌다.