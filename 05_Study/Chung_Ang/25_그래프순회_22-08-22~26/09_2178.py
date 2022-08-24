'''
N x M 배열
1은 이동할 수 있는 칸
0은 이동할 수 없는 칸
(1, 1) ~ (N, M) 최소의 칸수
'''

import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
_board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def valid_coord(r, c):
    return 0<=r<N and 0<=c<M

def bfs():
    visited[0][0] = True
    q = deque()
    q.append((0, 0, 1))
    while q:
        r, c, d = q.popleft()
        if r == N - 1 and c == M - 1:
            return d
        nd = d + 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if valid_coord(nr, nc):
                if not visited[nr][nc] and _board[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc, nd))

print(bfs())