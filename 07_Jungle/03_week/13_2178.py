from collections import deque
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
visited = [[0] * m for _ in range(n)]

def bfs():
    visited[0][0] = 1
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        if r == n - 1 and c == m - 1:
            return visited[n - 1][m - 1]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc]: continue
                if a[nr][nc] == '0': continue
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
print(bfs())
