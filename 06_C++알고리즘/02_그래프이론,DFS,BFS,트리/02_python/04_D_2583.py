import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

m, n, k = map(int, input().split())
a = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c):
    global cnt
    visited[r][c] = 1
    cnt += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < m and 0 <= nc < n:
            if a[nr][nc] or visited[nr][nc]: continue
            # cnt += 1
            dfs(nr, nc)
    return



for _ in range(k):
    c1, r1, c2, r2 = map(int, input().split())
    for r in range(r1, r2):
        for c in range(c1, c2):
            a[r][c] = 1 

ret = []
for i in range(m):
    for j in range(n):
        if a[i][j] or visited[i][j]: continue
        cnt = 0
        # cnt = 1
        dfs(i, j)
        ret.append(cnt)
print(len(ret))
print(*sorted(ret))
"""
<cnt += 1 의 위치>
1. cnt = 1 선언후 dfs내부 재귀함수 호출전 cnt += 1
2. cnt = 0 선언후 dfs내부 처음에 cnt += 1 
"""