# Graph

### 그래프(Graph)
- 하나의 데이터가 하나 이상의 다른 데이터와 연결되는 추상 데이터 타입.
- 데이터를 점(vertex) 또는 노드(Node)라고 한다.
- 각 점의 이름을 키(Key)라고 한다. 각 점에는 페이로드(Payload)라는 추가 데이터가 있기도 한다.
- 각 점 사이의 연결을 에지(Edge)라고 하며 점 사이를 이동하는 비용인 가중치(Weight)를 에지에 저장할 때도 있다.

<img width="467" alt="image" src="https://github.com/user-attachments/assets/735039fb-cdd7-4716-9384-2f326358709f" />


그래프에는 방향 그래프, 무방향 그래프, 완전 그래프 등의 다양한 타입이 있다. 

### 방향 그래프(Directed Graph)
- 각 에지에 방향이 있고 두 점을 이동할 때 에지의 방향을 따라서 이동하는 그래프. 양방향도 가능하다.
- 트위터처럼 팔로우 개념이 있는 소셜 네트워크를 나타낼 때 유용하다.

<img width="202" alt="image" src="https://github.com/user-attachments/assets/4b8c62d9-59a0-4e42-96ad-3dfa9ba83fed" />

### 무방향 그래프(Undirected Graph)
- 에지가 양방향인 그래프. 연결된 두 점은 어떤 방향이든 이동 가능하다.

```python
class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] # 4x4 이차원 리스트 만들고 저장. 


G1 = Graph(4)
# 0 == A, 1 == B, 2 == C, 3 == D
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1 # 그래프의 각 인덱스에 값 저장.
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print("G1 무방향 그래프")
for r in range(G1.size):
    for c in range(G1.size):
        print(G1.graph[r][c], end=' ')
    print()
# 1 1 1 0
# 1 0 1 0
# 1 1 0 1
# 1 0 1 0 
```
  
<img width="338" alt="image" src="https://github.com/user-attachments/assets/6e6f07e2-be6f-4387-aba8-ea68ba3398e1" />

### 완전 그래프(Complete Graph)
- 모든 점이 다른 모든 점과 연결된 그래프

### 불완전 그래프(Incomplete Graph)
- 전체 점 중 일부만 연결된 그래프 

### 경로(Path)
- 엣지로 연결된 점의 연속

### 사이클(Cycle)
- 시작점과 끝점이 같은 그래프의 경로 ``비순환 그래프 Acyclic Graph)``는 사이클이 포함되지 않은 그래프 

### 트리(Tree)
- 트리는 사실 그래프의 형태 중 하나. 트리는 방향(부모 자식 관계)이 있고 사이클은 없는 그래프.
- 자식 노드가 단 하나의 부모 노드만 가질 수 있는 제한있는 비순환 그래프.

### 그래프를 만드는 방법
- 에지 리스트
- 인접 행렬
- 인접 리스트 

### 에지 리스트(Edge List)
- 그래프의 각 에지를 연결된 두 개의 점으로 표현하는 자료구조

![image](https://github.com/user-attachments/assets/aba52b75-b29a-4394-936b-b3868bdeda95)

### 인접 행렬(Adjacency Matrix)
- 그래프의 점을 포함하는 행과 열의 이차원 배열
- 인접 행렬에서는 각 행과 열의 교집합으로 에지를 나타낸다.
- 연결된 점을 1로, 연결되지 않은 점을 0으로 나타낸다.
- ``인접(Adjacennt)``이란 두 점이 연결되었다는 뜻

```python
#   10 20 30 40
# 10 0 1 1 0 
# 20 1 0 1 0 
# 30 1 1 0 1 
# 40 0 0 1 0 
```

- 인접 행렬에는 성긴 셀 또는 빈 셀이라는 문제가 있다.
- 위 인접 행렬에는 8개의 빈 셀이 있다.
- 인접 행렬은 이런 빈 셀이 많아 메모리를 비효율적으로 사용하기 때문에 효율적인 데이터 저장 방법이 아니다.

### 인접 리스트(Adjacency List)
- 정렬되지 않은 리스트의 집합
- 리스트가 점 하나의 연결 상태

```python
# {
# 10 : [20, 30], 노드 10은 20, 30과 연결
# 20 : [10, 30],
# 30 : [10, 20, 40].
# 40 : [30[
# }
```

### 그래프를 사용해야 할 때
- 그래프에 점이나 에지를 추가하는 작업 0(1)을 따른다.
- 탐색, 삭제, 기타 알고리즘의 실행 시간은 그래프 구현 방법과 내부 자료구조에 따라 다르다.
- 기본 동작은 점이나 에지 같은 요소의 숫자, 이들의 조합에 따라 성능이 결정된다.
- 인스타, 트위터 같은 소셜 미디어 회사에서는 사람을 점으로 그들의 관계를 에지로 나타내는 그래프를 자주 사용한다.
- 네트워크 구성에도 자주 사용된다. 장치는 점으로 장치 사이의 유/무선 연결은 에지로 표현. 

## 깊이 우선 탐색 DFS Depth First Search
- 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘
- 자신과 연결된 노드 중 작은, 가까운 노드부터 방문. 반복. 갈 곳이 없다면 부른 곳으로 return

```python
# 이차원 배열 활용
graph = [ # 8x8 2차원 그래프 생성 
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def dfs(g, i, visited): # graph index visited list
  visited[i] = 1 # 시작하는 노드의 값은 1로 설정하여 방문을 true로 표시.
  print(chr(ord('A') + i), end = ' ') # chr(ord('A') + i 
  for j in range(len(graph)):
    if g[i][j] == 1 and not visited[j]: # i와j 노드가 서로 연결되어 있고 j노드를 아직 방문하지 않았다면
      dfs(g, j, visited) # j 매개변수로 재귀함수 호출. 

visited_dfs = [ 0 for _ in range(len(graph))] # 각 노드를 방문했는지 표시하는 list
dfs(graph, 6, visited_dfs) # 6 : G

# G D B A C E F H 
```
<img width="301" alt="image" src="https://github.com/user-attachments/assets/51d03b4e-d31a-44c0-bdce-5d283bad47bb" /><br>

## 너비 우선 탐색 BFS Breath First Search
- 이번에는 ``Queue``를 사용한다.
- ``큐(QUeue)``는 선입선출 구조의 선형 자료구조.
- 노드 자신과 연결된 노드부터 방문한다. 순서는 작은 순으로 설정.

### 디큐(Deque)
- 큐와 스택이 혼합된 개념. 양방향 큐로서, 앞뒤 방향에서 push와 pop이 가능하다.
- 가장 먼저 넣은 자료부터 꺼낼 수 있고 가장 마지막에 넣은 자료부터 꺼낼 수도 있다.

```python
from collections import deque

# 큐는 선입선출 구조다. 값을 추가하면 뒤에 추가되고 출력하면 먼저 들어간 값부터 나온다.

d = deque( [17, 55, 123] )
d.append(7) # 뒤(rear)에 추가 
d.appendleft(100) # 앞(front)에 추가 [100, 17, 55, 123, 7]
for _ in range(len(d)):
    print(d.popleft()) # deque에서 popleft() : 앞(front)부터 뽑기 pop() : 뒤(rear)부터 뽑기 
```

### 너비 우선 탐색 

```python
from collections import deque  # append, popleft : 먼저 들어온 자료 뽑기 pop : 나중 자료 뽑기 deque : 양방향 큐 

graph = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

def bfs(g, i, visited):
    q = deque([i]) # 방문 노드 추가 
    visited[i] = 1 # 방문 노드 true
    while q:
        i = q.popleft() # 가장 앞 노드 뽑기 
        print(chr(ord('A') + i), end=' ') 
        for j in range(len(graph)):
            if g[i][j] == 1 and not visited[j]:
                q.append(j) # 방문할 노드 디큐에 추가. E부터 시작하면 D,F 추가. D부터 뽑아서 반복 
                visited[j] = 1 # 방문 표시 

visited_bfs = [0 for _ in range(len(graph))]
bfs(graph, 4, visited_bfs) # 4 : E

# E D F B C G A H
```
