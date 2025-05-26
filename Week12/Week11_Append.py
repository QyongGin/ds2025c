# 2025-05-26

# deque : 양방향 큐
# append, popleft
# 안 보고 짤 수 있게 이해 필요

from collections import deque

d = deque([17, 55, 123])
d.append(7)
d.appendleft(100)
for _ in range(len(d)):
    print(d.popleft())

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

# 깊이 우선 탐색 DFS Depth First Search
# 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘.
# DFS Function create
def dfs(g, i, visited):
    visited[i] = 1 # visited node visited 표시
    print(chr(ord('A') + i ), end = ' ')
    for j in range(len(graph)): # 다 방문 했다면 자신을 호출한 행으로 이동.
        if g[i][j] == 1 and not visited[j]: # 1 : 연결되어있고 not visited 방문하지 않은 노드
            dfs(g,j,visited) # 조건 true 행 실행

# 너비 우선 탐색 BFS ( ex : sns )
# Use Queue
# Breath First Search

def bfs(g, i, visited):
    q = deque([i]) # queue 방문한 노드 순서 저장하는 변수
    visited[i] = 1
    while q:
        i = q.popleft() # 먼저 방문했던 노드 순서대로 내보내고 탐색
        print(chr(ord('A') + i), end=' ')
        for j in range(len(graph)):  # 다 방문 했다면 자신을 호출한 행으로 이동.
            if g[i][j] == 1 and not visited[j]:
                q.append(j)
                visited[j] = 1

# v_dfs = [0,0,0,0,0,0,0,0] A,B,C,D,E,F,G,H
visited_dfs = [ 0 for _ in range(len(graph))] # 방문 유무 0,1 list
visited_bfs = [0 for _ in range(len(graph))]
dfs(graph, 6, visited_dfs)
print()
bfs(graph, 4, visited_bfs)
