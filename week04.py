## 2025-03-31 week04

# 노드 -> 데이터를 보관하는 "필드" 다음 노드 위치를 가리키는 "포인터"
# 노드 a, b, c. a에는 필드와 다음 노드 b를 가리키는 포인터가 있다.
# 다음 노드가 없다면 포인터가 None을 가리킨다.

# 단일 링크드 리스트 -> 각 노드에 다음 요소를 가리키는 포인터만 존재.
# 이중 링크드 리스트 -> 각 노드에 다음 요소를 가리키는 포인터와 이전 요소를 가리키는 포인터 모두 있다.
# 환형 링크드 리스트 -> 마지막 노드에 첫 번째 노드를 가리키는 포인터가 있다. 반복에 유용.

# 배열 -> On 선형시간 / 링크드 리스트는 삽입삭제가 상수시간을 가진다. Oin
# 상수시간 > 로그 > 선형 > 선형로그 / 링크드 리스트는 삽입, 삭제에 강점을 갖고 있다.
# 링크드 리스트 노드 추가 or 제거 -> O(1) 배열은 -> O(n) => 링크드 리스트의 장점. 탐색은 모두 O(n)
# 링크드 리스트 -> 운영 체제의 메모리 관리 시스템, 데이터베이스, 회계, 재무, 금융 거래 시스템 광범위 사용.
# + 암호화폐를 뒷받침하는 웹 3.0의 기반 기술인 블록체인의 필수 요소다.

# 링크드 리스트 단점 -> 1. 배열보다 더 많은 메모리를 사용.
# 2. 임의 접근이 불가능. (상수 시간내 무작위로 데이터에 접근하는 경우) 반드시 헤드에서 시작해서 포인터를 따라 움직이며
# 원하는 요소에 도달할 때 까지 반복해야 한다.

class Node:
    def __init__(self, data, link=None): #
        self.data = data # 데이터
        self.link = link # 다음 노드를 가리키는 포인터(링크)

class LinkedList:
    def __init__(self):
        self.head = None # 필드가 하나.

    def append(self, data):
        if not self.head: # 객체 헤드값 none -> flase -> not으로 true.
            self.head = Node(data) # head는 Node 객체 (필드:8 | 링크:None)를 가리키게 된다.
            return
        current = self.head #
        while current.link: #
            current = current.link # 현재 current가 갖고있는 링크를 이동.
        current.link = Node(data) # Node (데이터 10 | 링크:None)

    def __str__(self): # 노드를 출력하기 위해.
        # current = self.head
        # while current is not None:
        #     print(current.data)
        #     current = current.link
        # return "end"
        current = self.head
        out_texts = ""
        while current is not None:
            # out_texts = out_texts + str(current.data) + " -> " 1 번째 방법.
            out_texts = out_texts + f"{current.data} -> " # 2 번째 방법.
            current = current.link
        return out_texts + "END"

ll = LinkedList() #LinkedList() 객체 생성
ll.append(8)
ll.append(10)
ll.append(-9) # current.link는 현재 Node (데이터 10)
print(ll)



