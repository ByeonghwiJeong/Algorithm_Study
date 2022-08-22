import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


N, M, R = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)
ans = [0] * (N + 1)
order = 1
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort(reverse=True)

def dfs(graph, v, visited):
    global order
    visited[v] = True
    ans[v] = order
    order += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, R, visited)

print(*ans[1:], sep='\n')