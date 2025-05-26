# Graph

### 그래프(Graph)
하나의 데이터가 하나 이상의 다른 데이터와 연결되는 추상 데이터 타입.<br>
데이터를 점(vertex) 또는 노드(Node)라고 한다.<br>
각 점의 이름을 키(Key)라고 한다. 각 점에는 페이로드(Payload)라는 추가 데이터가 있기도 한다.
각 점 사이의 연결을 에지(Edge)라고 하며 점 사이를 이동하는 비용인 가중치(Weight)를 에지에 저장할 때도 있다.
<img width="467" alt="image" src="https://github.com/user-attachments/assets/735039fb-cdd7-4716-9384-2f326358709f" />
<br>
그래프에는 방향 그래프, 무방향 그래프, 완전 그래프 등의 다양한 타입이 있다. 

### 방향 그래프(Directed Graph)
각 에지에 방향이 있고 두 점을 이동할 때 에지의 방향을 따라서 이동하는 그래프. 양방향도 가능하다.
트위터처럼 팔로우 개념이 있는 소셜 네트워크를 나타낼 때 유용하다. <br>
<img width="202" alt="image" src="https://github.com/user-attachments/assets/4b8c62d9-59a0-4e42-96ad-3dfa9ba83fed" />
<br>
### 무방향 그래프(Undirected Graph)
에지가 양방향인 그래프. 연결된 두 점은 어떤 방향이든 이동 가능하다.<br>
<img width="338" alt="image" src="https://github.com/user-attachments/assets/6e6f07e2-be6f-4387-aba8-ea68ba3398e1" />

## 깊이 우선 탐색 DFS Depth First Search
그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘 <br>
DFS 함수를 생성.

```python
# 이차원 배열 활용
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

def dfs(g, i, visited): # graph index visited list
  visited[i] = 1 # 시작하는 노드의 값은 1로 설정하여 방문을 true로 표시.
  print(chr(ord('A') + i), end = ' ')
  for j in range(len(graph)):
    if g[i][j] == 1 and not visited[j]: # i와j 노드가 서로 연결되어 있고 j노드를 아직 방문하지 않았다면
      dfs(g, j, visited)

visited_dfs = [ 0 for _ in range(len(graph))] # 각 노드를 방문했는지 표시하는 list
dfs(graph, 6, visited_dfs)

```
<img width="301" alt="image" src="https://github.com/user-attachments/assets/51d03b4e-d31a-44c0-bdce-5d283bad47bb" /><br>
노드를 반복했는지 표시하는 리스트 생성. ```visited_dfs = [ 0 for _ in range(len(graph))]```<br> 
```_ in range```는 변수 i를 사용할 필요가 없어서 언더바```_```로 생략하였다.<br>
각 반복마다 0을 추가해서 최종적으로 리스트를 만든다. <br><br>
dfs 함수에 만들어둔 graph와 시작 index, 방문 리스트를 매개 변수로 보낸다.
시작하는 노드를 i라 칭하고 방문 리스트의 i번째 노드를 1로 설정해서 방문을 표현한다.
```ord('A')```로 'A' 문자의 정수값 65를 반환하고 정수 i를 더하여 현재 시작 노드의 정수값을 만들고 ```chr```로 정수값을
다시 문자로 변환하여 각 노드를 문자로 표현한다.<br><br>
그래프의 길이만큼 반복을 실행한다. ```g[i][j] 


