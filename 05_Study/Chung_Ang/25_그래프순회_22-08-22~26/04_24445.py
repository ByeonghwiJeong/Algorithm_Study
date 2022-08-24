from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
ans = [0] * (N+1)
order = 1
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort(reverse=True)

def bfs(start):
    global order
    q = deque()
    q.append(start)
    visited[start] = True
 
    while q:
        v = q.popleft()
        ans[v] = order
        order += 1  
        for next in graph[v]:
            if not visited[next]:
                q.append(next)
                visited[next] = True

bfs(R)
print(*ans[1:], sep='\n')