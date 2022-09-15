from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

N, K = map(int, input().split())
visited = [0] * 100001

def bfs(s):
    visited[s] = 1
    q = deque()
    q.append((s, 0))
    while q:
        x, t = q.popleft()
        if x == K:
            return t
        nt = t + 1
        for nx in [x - 1, x + 1, x * 2]:
            if 0 <= nx <= 100000:
                if not visited[nx]:
                    q.append((nx, nt))
                    visited[nx] = 1

print(bfs(N))
