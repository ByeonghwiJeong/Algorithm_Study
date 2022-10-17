import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0 <= nr < N and 0 <= nc < M):
            if a[nr][nc] == 0 or visited[nr][nc]: continue
            visited[nr][nc] = 1
            dfs(nr, nc)

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    a = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        a[Y][X] = 1
    for r in range(N):
        for c in range(M):
            if a[r][c] == 0 or visited[r][c]: continue
            dfs(r, c)
            cnt += 1
    print(cnt)