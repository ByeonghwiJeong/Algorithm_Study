from collections import deque
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)
for i in range(n + 1):
    adj[i].sort()

def dfs(n):
    global visited
    visited[n] = 1
    print(n, end=' ')
    for nxt in adj[n]:
        if visited[nxt]: continue
        dfs(nxt)
    return

def bfs(n):
    global visited
    visited[n] = 1
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        print(x, end=' ')
        for nxt in adj[x]:
            if visited[nxt]: continue
            visited[nxt] = 1
            q.append(nxt)
    return


visited = [0] * (n + 1)
dfs(v)
print()
visited = [0] * (n + 1)
bfs(v)