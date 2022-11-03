from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [input().rstrip() for _ in range(n)]
# visited = [[0] * m for _ in range(n)]
ret = 0
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


def bfs(r, c):
    global ret
    visited = [[0] * m for _ in range(n)]
    visited[r][c] = 1
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc]: continue
                if a[nr][nc] == 'W': continue
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
                ret = max(ret, visited[nr][nc])

for i in range(n):
    for j in range(m):
        if a[i][j] == 'L': bfs(i, j)

print(ret - 1)