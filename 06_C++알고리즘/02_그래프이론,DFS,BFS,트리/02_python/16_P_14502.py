import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c):
    global visited
    if a[r][c] == 1 or visited[r][c]: return
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            dfs(nr, nc)


def solve():
    global visited
    visited = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2: dfs(i, j)
    ret = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0 and visited[i][j] == 0:
                ret += 1
    return ret

b = []

for i in range(n):
    for j in range(m):
        if not a[i][j]: b.append((i, j))
ans = 0
for i in range(len(b)):
    for j in range(i):
        for k in range(j):
            a[b[i][0]][b[i][1]] = 1
            a[b[j][0]][b[j][1]] = 1
            a[b[k][0]][b[k][1]] = 1
            ans = max(ans, solve())
            a[b[i][0]][b[i][1]] = 0
            a[b[j][0]][b[j][1]] = 0
            a[b[k][0]][b[k][1]] = 0
print(ans)

