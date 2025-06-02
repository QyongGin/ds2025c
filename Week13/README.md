### 깊이 우선 탐색 stack 없이 재귀함수로 구하기
```python
# dfs 깊이 우선 탐색

def dfs(g, current, visited): # 현재 노드 current에서 dfs를 통해 연결된 모든 정점 방문
    visited.append(current) # 현재 노드 방문 처리
    for vertex in range(graph_size):
        if g.graph[current][vertex] > 0 and vertex not in visited:
        # 가중치가 0보다 크고 아직 방문하지 않아서 list에 없다면 
            dfs(g, vertex, visited) # 재귀 함수 호출

def find_vertex(g, find_vtx) : # 도시 연결 확인  
    visited_array = list() # 방문 리스트 
    dfs(g, 0, visited_array) # 0번 도시 출발
    return find_vtx in visited_array # True or False 특정 도시find_vtx 도달하면 True
```
예시 그래프
```python
g.graph = [
  [0, 1, 1, 0],  # 0번 노드는 1번, 2번과 연결
  [1, 0, 1, 0],  # 1번 노드는 0번, 2번과 연결
  [1, 1, 0, 1],  # 2번 노드는 0번, 1번, 3번과 연결
  [0, 0, 1, 0]   # 3번 노드는 2번과만 연결
]
```
- 0과 1 연결 -> 1번 노드 방문 ``visited = [0, 1]``
- 1과 2 연결 -> 2번 노드 방문 ``visited = [0, 1, 2]``
- 2와 3 연결 -> 3번 노드 방문 ``visited = [0, 1, 2, 3]``
- ``find_vertex(g,3)``이라 하면 ``3 in [0, 1, 2, 3]``이므로 ``True`` 반환
<img width="114" alt="image" src="https://github.com/user-attachments/assets/cc7db701-6d1d-45c8-86b3-73463ea81611" />

- ``g1.graph[incheon][seoul] = 10; g1.graph[incheon][gangneung] = 15`` 가중치가 0보다 크므로 연결됨.

### 크루스칼 알고리즘 오름차순
- 가중치가 낮은 순서대로 엣지 연결, 사이클이 생기는 순간 그 엣지는 가중치 0 설정
### 역크루스칼 알고리즘 내림차순
- 큰 엣지부터 삭제하면서 연결이 끊어지는지 확인한다.

### 서로소
- disjoint set 공통 원소 없는 두 집합  
### Union 
- x가 속한 집합과 y가 속한 집합을 합친다. Union(1,2)
### find 
- x가 속한 집합의 대푯값 반환, 트리 이용 구현하므로 대푯값은 루트 노드 번호(가장 작은 값)










