'''
입력)
- T 테스트수
- 가로길이 M [1 \ 50], 세로 N[1 \ 50], 배추수 K
- 배추위치 X[0, M-1],  Y[0, N-1]

'''
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def valid_coord(r, c):
    return 0 <= r < N and 0 <= c < M

def dfs(r, c):
    global visited, _board
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if valid_coord(nr, nc):
            if not visited[nr][nc] and _board[nr][nc]:
                dfs(nr, nc)

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    _board = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        _board[Y][X] = 1
    for r in range(N):
        for c in range(M):
            if not visited[r][c] and _board[r][c]:
                cnt += 1
                dfs(r, c)
    print(cnt)