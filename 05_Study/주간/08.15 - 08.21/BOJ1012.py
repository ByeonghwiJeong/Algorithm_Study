'''
배추밭 지렁이문제
0 : 배추 X
1 : 배추 O
M, N ~ [1, 50]

'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def coord_vaild(r, c):
    return 0<= r < N and 0 <= c < M
# M:X,c , N:Y,r

def dfs(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if coord_vaild(nr, nc):
            if _board[nr][nc] == 1:
                _board[nr][nc] = 0
                dfs(nr, nc)
    return

for _ in range(int(input())):
    M, N, K = map(int, input().split())
    _board = [[0] * M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        _board[Y][X] = 1
    
    for i in range(N):
        for j in range(M):
            if _board[i][j] == 1:
                _board[i][j] = 0
                dfs(i, j)
                cnt += 1
    print(cnt)
