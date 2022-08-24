import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)
dfs_ans = []
bfs_ans = []
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort()

def dfs(start):
    dfs_visited[start] = True
    dfs_ans.append(start)
    for next in graph[start]:
        if not dfs_visited[next]:
            dfs(next)

def bfs(start):
    q = deque()
    q.append(start)
    bfs_visited[start] = True
    bfs_ans.append(start)
    while q:
        x = q.popleft()
        for next in graph[x]:
            if not bfs_visited[next]:
                q.append(next)
                bfs_visited[next] = True
                bfs_ans.append(next)

dfs(V)
bfs(V)
print(*dfs_ans)
print(*bfs_ans)