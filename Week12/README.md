# 그래프의 응용

### 최소 신장 트리 개념
- 신장 트리(Spanning Tree)는 최소 간선으로 그래프의 모든 정점이 연결되는 그래프

### 최소 비용 신장 트리
- 가중치 그래프에서 만드는 신장 트리 중 합계가 최소인 그래프.
- 구현하는 방법은 크루스컬(Kruskal) 알고리즘, 프림(Prim) 알고리즘 등이 있다.

![image](https://github.com/user-attachments/assets/3b525dd0-3e97-44d5-a851-e5cb96c6ddd1)


### 전체 비용이 나온 가중치 그래프 구현 예시

```python
class Graph:
	def __init__ (self, size):
		self.graph = [[0 for _ in range(size)] for _ in range(size)]

g1 = None
name_ary = ['인천', '서울', '강릉', '대전', '광주', '부산']
incheon, seoul, gangneung, daejeon, gwangju, busan = 0, 1, 2, 3, 4, 5


graph_size = 6
g1 = Graph(graph_size) # 6x6 2차원 그래프 
g1.graph[incheon][seoul] = 10; g1.graph[incheon][gangneung] = 15
g1.graph[seoul][incheon] = 10; g1.graph[seoul][gangneung] = 40; g1.graph[seoul][daejeon] = 11; g1.graph[seoul][gwangju] = 55
g1.graph[gangneung][incheon] = 15; g1.graph[gangneung][seoul] = 40; g1.graph[gangneung][daejeon] = 12
g1.graph[daejeon][seoul] = 11; g1.graph[daejeon][gangneung] = 12; g1.graph[daejeon][gwangju] = 20; g1.graph[daejeon][busan] = 30
g1.graph[gwangju][seoul] = 55; g1.graph[gwangju][daejeon] = 20; g1.graph[gwangju][busan] = 28
g1.graph[busan][daejeon] = 30; g1.graph[busan][gwangju] = 28

print('도시 간 도로 건설을 위한 전체 연결도')
print_graph(g1)
```
![image](https://github.com/user-attachments/assets/62f4315a-2d4d-44f2-ad2d-54a26216f813)

### 가중치와 간선 목록 생성
- 가중치와 간선을 별도 배열로 만드는 예
```python
edge_ary = [] # 가중치 리스트 생성
for i in range(graph_size):
  for k in range(graph_size): # 6x6
    if g1.graph[i][k] != 0: # 연결되었다면 
      edge_ary.append([g1.graph[i][k], i, k])

# edges.sort(reverse=False) 오름차순
edges.sort(reverse=True) # 내림차순  가중치가 큰 값부터 출력
 
# [[가중치, 'i', 'k'], [가중치, 'i', 'k']]
# [[55, 4, 1], [55, 1, 4], [40, 2, 1], [40, 1, 2], [30, 5, 3], [30, 3, 5], [28, 5, 4], [28, 4, 5],
  [20, 4, 3], [20, 3, 4], [15, 2, 0], [15, 0, 2], [12, 3, 2], [12, 2, 3], [11, 3, 1], [11, 1, 3],
  [10, 1, 0], [10, 0, 1]]
```

### 중복 간선 제거 
- 현재 서울과 광주의 가중치가 55다. 서울 입장에서 55와 광주 입장에서 55라는 가중치가 입력된 상태.
- 출력도 그럼 중복으로 나타난다. ``[[55, 4, 1], [55, 1, 4]`` 이를 해결하고자 홀수 값만 출력하겠다.

```python
new_ary = list()

# 1 : 시작값 -> 1번 인덱스부터 시작 len(edge_ary) 가중치 그래프 끝가지 2: 간격 -> 2씩 건너 뛰기 -> 1, 3, 5
for i in range(1, len(edge_ary), 2): 
	new_ary.append(edge_ary[i])
print(new_ary)
# [[55, 1, 4], [40, 1, 2], [30, 3, 5], [28, 4, 5], [20, 3, 4], [15, 0, 2], [12, 2, 3], [11, 1, 3], [10, 0, 1]]
```

### 최소 비용 신장 트리
- 크루스칼 알고리즘 변형한 방식 
```python
# 깊이 우선 탐색 DFS
# 정점 연결됐는지 확인
def find_vertex(g, find_vtx) :
	stack = list() 
	visited_ary = list() # 방문한 정점 리스트 

	current = 0	# 시작 정점
	stack.append(current) # 스택에 추가 
	visited_ary.append(current) # 방문 추가 

	while stack: # 스택이 비어있지 않다면 
		next = None
		for vertex in range(graph_size):
			if g.graph[current][vertex] != 0:  # 가중치가 0이 아니다 -> 연결 
				if vertex in visited_ary:	# 방문 리스트에 있다면 
					pass
				else :			# 방문한 적이 없으면
					next = vertex  #  다음 정점으로 지정
					break # for문 끝내기 

		if next is not None:				# 다음에 방문할 정점이 있는 경우
			current = next # 현재 위치는 이전 정점과 연결된 정점 
			stack.append(current)  # push
			visited_ary.append(current)  # push
		else :					# 다음에 방문할 정점이 없는 경우
			current = stack.pop() # 이전 정점으로 돌아가기 (백트래킹)

	if find_vtx in visited_ary: # 찾고자한 find_vtx가 방문 목록에 있다면 
		return True
	else :
		return False


index = 0 # new_ary 리스트의 현재 위치 0(인천)부터 시작. .sort(reverse=True) 내림차순이라면 [55, 1, 4]부터 시작 
while len(new_ary) > graph_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복, 노드가 6개라면 5개의 엣지가 최소 신장 엣지 
	start = new_ary[index][1] # new_ary -> [55, 4, 1] 가중치, 시작노드, 끝노드 형식 저장 [index=0]이라면 가중치 55부터 시작.
	end = new_ary[index][2] # [55][4]
	save_cost = new_ary[index][0] # index는 간선 0번째 간선인 55, 4, 1에서 [0]인덱스(가중치) 저장 

	g1.graph[start][end] = 0
	g1.graph[end][start] = 0

	start_reachable = find_vertex(g1, start) # start 정점이 그래프에서 끊켰는지
	end_reachable = find_vertex(g1, end) # enr 정점이 끊켰는지 

	if start_reachable and end_reachable : # 둘 다 연결되어 있다면 
		del new_ary[index] #  # new_ary -> [55, 4, 1]에서 0번 index 가중치를 제거 -> 간선 제거
	else:
		g1.graph[start][end] = save_cost # [4] [1] 에 가중치 55 저장 
		g1.graph[end][start] = save_cost # 양방향 그래프이기 때문에 저장. 하나의 가선. 
		index = index + 1
```

### 총 가중치 
```python
total_cost = 0
for i in range(graph_size):
	for k in range(graph_size):
		if g1.graph[i][k] != 0:
			total_cost = total_cost + g1.graph[i][k]

total_cost = total_cost // 2 # 양방향 그래프니까 // 2 "//"는 몫을 구하는 연산자 
print(f"최소 비용의 도로 건설 비용 :  {total_cost}")

# 최소 신장 엣지 만들기
for cost, s, e in edges:
    if ds.merge(s, e):
        mst_edges.append((cost, s, e)) # 가중치 도시들 추가, 최소 간선 추가
        mst_cost = mst_cost + cost # 최소 비용 업데이트

# 세로 그래프 만들기 최소 신장 트리
mst_graph = Graph(graph_size)
for cost, s, e in mst_edges:
    mst_graph.graph[s][e] = cost # start, end 도시 cost 할당
    mst_graph.graph[e][s] = cost
```















