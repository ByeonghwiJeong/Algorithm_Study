import sys
sys.setrecursionlimit(10 ** 7)
from collections import deque

N, M = map(int, input().split())
_board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def bfs():
    q = deque()
    q.append((0, 0, 1, 1))
    visited[0][0][0] = 1
    while q:
        r, c, d, t = q.popleft()
        if r == N - 1 and c == M - 1:
            return d
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            nd = d + 1
            """ (다음row, 다음col, 다음distance, 벽부심유무)"""
            # 벽부심OK - 0 / 벽부심NO - 1
            if 0 <= nr < N and 0 <= nc < M:
                if _board[nr][nc] == 0:
                    if t == 1 and visited[nr][nc][0] == 0:  # 벽안부신경우 [x][x][0]
                        q.append((nr, nc, nd, t))
                        visited[nr][nc][0] = 1
                    elif t == 0 and visited[nr][nc][1] == 0: # 벽부신경우 [x][x][1]
                        q.append((nr, nc, nd, t))
                        visited[nr][nc][1] = 1
                elif _board[nr][nc] == 1 and t == 1 and visited[nr][nc][1] == 0:   # 벽안부신경우 > 벽부시기 [x][x][1]
                    q.append((nr, nc, nd, 0))
                    visited[nr][nc][1] = 1
    return -1

print(bfs())