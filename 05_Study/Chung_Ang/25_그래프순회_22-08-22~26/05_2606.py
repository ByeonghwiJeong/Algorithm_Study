import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input()) # 노드
M = int(input()) # 간선
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
ans = 0
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(x):
    global ans
    visited[x] = True
    for next in graph[x]:
        if not visited[next]:
            ans += 1
            dfs(next)

dfs(1)
print(ans)