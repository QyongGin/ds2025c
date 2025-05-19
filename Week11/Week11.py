# Graph

## Week11

# 깊이 우선 탐색 DFS Deeps First Search
# DFS Function create

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

# 작은 순 실행. G부터 시작하면 가장 먼저 열결된 부분부터. D.
def dfs(g, i, visited):
    visited[i] = 1 # visited node visited 표시
    print(chr(ord('A') + i ), end = ' ')
    for j in range(len(graph)): # 다 방문 했다면 자신을 호출한 행으로 이동.
        if g[i][j] == 1 and not visited[j]: # 1 : 연결되어있고 not visited 방문하지 않은 노드
            dfs(g,j,visited) # 조건 true 행 실행

# v_dfs = [0,0,0,0,0,0,0,0] A,B,C,D,E,F,G,H
visited_dfs = [ 0 for _ in range(len(graph))]
dfs(graph, 6, visited_dfs)