import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

def dfs(r, c, d):
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if visited[nr][nc] or a[nr][nc] <= d: continue
            dfs(nr, nc, d)
    return
ret = 0
for d in range(101): # 1 ~ 100 : X >>> 0 ~ 100 : O
    visited = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] or a[i][j] <= d: continue
            dfs(i, j, d)
            cnt += 1
    ret = max(ret, cnt)
print(ret)
"""
방문체크 visited --- 초기화 완전 주의
"""