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

def dfs(g, i, visited):
    visited[i] = 1 # visited node visited 표시
    print(chr(ord('A') + i ), end = ' ')
    for j in range(len(graph)):
        if g[i][j] == 1 and not visited[j]:
            dfs(g,j,visited)

# v_dfs = [0,0,0,0,0,0,0,0] A,B,C,D,E,F,G,H
visited_dfs = [ 0 for _ in range(len(graph))]
dfs(graph, 4, visited_dfs)