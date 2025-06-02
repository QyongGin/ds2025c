# 2025-06-02

# 시험 하이테크센터 강당 16일 월요일 17:00 1~14주차 내용

class Graph:
    def __init__ (self, size):
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

class DisjoinSet: # 서로소 집합, 크루스칼 알고리즘을 위한 유틸리티 클래스
    def __init__(self, n): # 정점 개수 받기
        self.parent = [i for i in range(n)] # n개 원소를 가진 리스트 생성

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def merge(self, x, y): # 합치기
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root != y_root:
            self.parent[y_root] = x_root
            return True
        return False

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

## dfs 깊이 우선 탐색
# 나중에 너비 우선 탐색으로도 시도

# def dfs(g, current, visited): # 현재 노드 current에서 dfs를 통해 연결된 모든 정점 방문
#     visited.append(current) # 현재 노드 방문 처리
#     for vertex in range(graph_size):
#         if g.graph[current][vertex] > 0 and vertex not in visited:
#         # 가중치가 0보다 크고 아직 방문하지 않아서 list에 없다면
#             dfs(g, vertex, visited) # 재귀 함수 호출
#
# def find_vertex(g, find_vtx) : # 도시 연결 확인
#     visited_array = list() # 방문 리스트
#     dfs(g, 0, visited_array) # 0번 도시 출발
#     return find_vtx in visited_array # True or False 특정 도시find_vtx 도달하면 True

# 전체 비용 나온 가중치 그래프
g1 = None
cities = ['인천', '서울', '강릉', '대전', '광주', '부산']
incheon, seoul, gangneung, daejeon, gwangju, busan = 0, 1, 2, 3, 4, 5

graph_size = 6
g1 = Graph(graph_size)
g1.graph[incheon][seoul] = 10; g1.graph[incheon][gangneung] = 15 # 15 연결하면 사이클이 생기므로 0처리
g1.graph[seoul][incheon] = 10; g1.graph[seoul][gangneung] = 40; g1.graph[seoul][daejeon] = 11; g1.graph[seoul][gwangju] = 55
g1.graph[gangneung][incheon] = 15; g1.graph[gangneung][seoul] = 40; g1.graph[gangneung][daejeon] = 12
g1.graph[daejeon][seoul] = 11; g1.graph[daejeon][gangneung] = 12; g1.graph[daejeon][gwangju] = 20; g1.graph[daejeon][busan] = 30
g1.graph[gwangju][seoul] = 55; g1.graph[gwangju][daejeon] = 20; g1.graph[gwangju][busan] = 28
g1.graph[busan][daejeon] = 30; g1.graph[busan][gwangju] = 28

# 크루스칼 알고리즘 오름차순
# 가중치가 낮은 순서대로 엣지 연결, 사이클이 생기는 순간 그 엣지는 가중치 0 설정

# 서로소 disjoint set 공통 원소 없는 두 집합
# Union x가 속한 집합과 y가 속한 집합을 합친다. Union(1,2)
# find x가 속한 집합의 대푯값 반환, 트리 이용 구현하므로 대푯값은 루트 노드 번호(가장 작은 값)
#



print('도시 간 도로 건설을 위한 전체 연결도')
print_graph(g1)

edges = []  # 결과적으로 2d list
for i in range(graph_size) :
	for j in range(graph_size) :
		if g1.graph[i][j] != 0 :
			edges.append([g1.graph[i][j], i, j])
print(edges)

edges.sort(reverse=False) # 오름차순
# [[10, 0, 1], [15, 0, 2], [10, 1, 0], [40, 1, 2], [11, 1, 3], [55, 1, 4], [15, 2, 0], [40, 2, 1], [12, 2, 3], [11, 3, 1], [12, 3, 2], [20, 3, 4], [30, 3, 5], [55, 4, 1], [20, 4, 3], [28, 4, 5], [30, 5, 3], [28, 5, 4]]
# [[10, 0, 1], [10, 1, 0], [11, 1, 3], [11, 3, 1], [12, 2, 3], [12, 3, 2], [15, 0, 2], [15, 2, 0], [20, 3, 4], [20, 4, 3], [28, 4, 5], [28, 5, 4], [30, 3, 5], [30, 5, 3], [40, 1, 2], [40, 2, 1], [55, 1, 4], [55, 4, 1]]

print(edges)

# 간선만큼 빼고 지우는 코드들
# new_ary = list()
# for i in range(1, len(edges), 2):
# 	# new_ary.append(edges[i])
# print(# new_ary)
#
# index = 0
# while len(# new_ary) > graph_size - 1:	# 간선의 개수가 '정점 개수-1'일 때까지 반복
# 	start = # new_ary[index][1]
# 	end = # new_ary[index][2]
# 	save_cost = # new_ary[index][0]
#
# 	g1.graph[start][end] = 0
# 	g1.graph[end][start] = 0
#
# 	start_reachable = find_vertex(g1, start)
# 	end_reachable = find_vertex(g1, end)
#
# 	if start_reachable and end_reachable :
# 		del # new_ary[index]
# 	else:
# 		g1.graph[start][end] = save_cost
# 		g1.graph[end][start] = save_cost
# 		index = index + 1 # 간선 연결했으니

ds = DisjoinSet(graph_size)
mst_edges = list() # 최소 신장 트리
mst_cost = 0

# 최소 신장 엣지 만들기
for cost, s, e in edges:
    if ds.merge(s, e):
        mst_edges.append((cost, s, e)) # 가중치 도시들 추가, 최소 간선 추가
        mst_cost = mst_cost + cost # 최소 비용 업데이트

# 세로 그래프 만들기 최소 신장 트리
mst_graph = Graph(graph_size)
for w, s, e in mst_edges:
    mst_graph.graph[s][e] = w # start, end 도시 cost 할당
    mst_graph.graph[e][s] = w



print()
print('최소 비용의 도로 연결도')
print()
print_graph(mst_graph)
print(f"최소 비용의 도로 건설 비용 :  {mst_cost}")

# total_cost = 0
# for i in range(graph_size):
# 	for j in range(graph_size):
# 		if g1.graph[i][j] != 0:
# 			total_cost = total_cost + g1.graph[i][j]
#
# total_cost = total_cost // 2
# print(f"최소 비용의 도로 건설 비용 :  {total_cost}")



