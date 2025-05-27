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
- 보통 HTML과 XML은 태그를 중첩할 수 있어 트리로 표현하며, 각 노드는 HTML이나 XML의 요소를 나타낸다.
- 문서 객체 모델(DOM Document Object Model) : XML이나 HTML 문서를 트리로 나타내는 언어 독립적 인터페이스. JS가 사용.
<img width="443" alt="image" src="https://github.com/user-attachments/assets/020ace5b-03c4-4f05-b474-33f4bf38fc1a" />

- 산술 표현식 역시 트리 형태로 분석 가능하다.
- 2 + 3 * 4를 예로 든다. 트리 아래로 곱셈을 내리고 3 * 4를 계산 후 2 + 12를 계산해 답을 얻는다. 이런 트리가 파스 트리다.
- 파스 트리(Parse Tree) : 표현식 평가 규칙과 같은 일정한 문법에 따라 데이터를 저장하는 정렬된 트리.
<img width="186" alt="image" src="https://github.com/user-attachments/assets/75d37b12-18b4-4533-a77f-1b15d663ffb7" />

### 이진 탐색의 장점
- 해시 테이블은 충돌로 인해 실제 저장하는 데이터보다 열 배 이상의 공간을 사용할 수 있다. 데이터를 순서대로 저장하지 않아, 순서에 따라 이동하지 못한다.
- 반면, 이진 탐색 트리는 메모리를 낭비하지 않는다. 데이터의 정렬된 순서나 역순으로 빠르게 이동 가능하다.

# 트리 만들기

