'''

세로 길이 N, 가로길이 M, 쓰레기 개수 K
'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, M, K = map(int, input().split())
_board = [[0] * M for _ in range(N)]

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)


for _ in range(K):
    r, c = map(lambda x: int(x) - 1, input().split())
    _board[r][c] = 1

def coord_vaild(r, c):
    return 0<= r < N and 0 <= c < M

def dfs(r, c):
    global cnt
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if coord_vaild(nr, nc):
            if _board[nr][nc]:
                cnt += 1
                _board[nr][nc] = 0
                dfs(nr, nc)
    return

ans = 0

for i in range(N):
    for j in range(M):
        if _board[i][j]:
            cnt = 1
            _board[i][j] = 0
            dfs(i, j)
            ans = max(ans, cnt)
print(ans)