### 깊이 우선 탐색 stack 없이 재귀함수로 구하기
```python
# dfs 깊이 우선 탐색
def dfs(g, current, visited): # 현재 노드 current에서 dfs를 통해 연결된 모든 정점 방문
    visited.append(current) # 현재 노드 방문 처리
    for vertex in range(graph_size):
        if g.graph[current][vertex] > 0 and vertex not in visited:
        # 가중치가 0보다 크고 아직 방문하지 않아서 list에 없다면 
            dfs(g, vertex, visited) # 재귀 함수 호출
# 가장 먼저 연결된 정점부터 파고들어 방문 리스트에 추가. 현재 연결된 정점이 나온다.

# 정점 찾기 
def find_vertex(g, find_vtx) : # 도시 연결 확인  
    visited_array = list() # 방문 리스트 
    dfs(g, 0, visited_array) # 0번 도시 출발해서 연결된 정점들 구하기 
    return find_vtx in visited_array # True or False 특정 도시(find_vtx)가 존재하면 True
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

### 크루스칼 알고리즘 (오름차순)
- 가중치가 낮은 순서대로 엣지 연결, 사이클이 생기는 순간 그 엣지는 가중치 0 설정
### 역크루스칼 알고리즘 (내림차순)
- 큰 엣지부터 삭제하면서 연결이 끊어지는지 확인한다.

### 서로소
- disjoint set 공통 원소 없는 두 집합  
### Union 
- x가 속한 집합과 y가 속한 집합을 합친다. Union(1,2)
### find 
- x가 속한 집합의 대푯값 반환, 트리 이용 구현하므로 대푯값은 루트 노드 번호(가장 작은 값)

### DisJoinSet

```python
# 서로소 집합, Union-Find 구조 
# 크루스칼 알고리즘을 위한 유틸리티 클래스

class DisjoinSet: 
    def __init__(self, n): # 정점 개수 받기
        self.parent = [i for i in range(n)] # n개 정점 가진 리스트 생성

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # 집합의 대표(루트 노드)를 재귀적으로 찾아간다. 
        return self.parent[x] # 부모를 루트 노드로 직접 연결하여 이후 탐색 속도를 올린다.

    def merge(self, x, y): # 두 집합 합치기 
        x_root = self.find(x) # x가 속한 집합의 대표 노드(루트) 찾기
        y_root = self.find(y)

        if x_root != y_root: # 서로 다른 집합에 속해 있으면 
            self.parent[y_root] = x_root # 한 쪽의 루트를 다른 쪽의 부모로 설정하여 병합 
            return True # 병합 성공 
        return False

# 그래프 출력
def print_graph(g) :
    print(' ', end = ' ')
    for v in range(len(g.graph)) :
        print(cities[v], end =' ')
    print()
    for row in range(len(g.graph)) :
        print(cities[row], end =' ')
        for col in range(len(g.graph)) :
            print(f"{g.graph[row][col]:2d}", end=' ')
        print()
    print()

ds = DisjoinSet(graph_size)

# 예시
ds = DisjoinSet(5)  # 0~4번 노드를 가지는 집합 생성

ds.merge(0, 1)  # 0과 1을 병합 → 같은 집합이 됨
ds.merge(1, 2)  # 1과 2를 병합 → 0,1,2는 같은 집합
ds.merge(3, 4)  # 3과 4를 병합

print(ds.find(2))  # 결과: 0 (0~2는 같은 집합이므로 루트는 0)
print(ds.find(4))  # 결과: 3 (3, 4는 같은 집합이므로 루트는 3)


```

### 크루스칼 알고리즘에서의 활용
- 간선을 가중치 기준으로 정렬하고 하나씩 선택하며 ``merge(u,v)``가 True일 때만 트리에 포함
- False면 사이클이 발생하므로 무시 









