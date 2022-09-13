'''
보통 DFS로 문제를 푸는데
BFS로 문제를 접근해봤다.

대각선 연결 체크 주의
'''
from collections import deque
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
_board = [list(map(int, input().split())) for _ in range(N)]

dr = (0, 1, 0, -1, 1, -1, 1, -1)
dc = (1, 0, -1, 0, 1, 1, -1, -1)

def bfs(r, c):
    _board[r][c] = 0
    q = deque()
    q.append((r, c))
    while q:
        sr, sc = q.popleft()
        for i in range(8):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0 <= nr < N and  0 <= nc < N:
                if _board[nr][nc]:
                    q.append((nr, nc))
                    _board[nr][nc] = 0

result = 0

for i in range(N):
    for j in range(N):
        if _board[i][j]:
            bfs(i, j)
            result += 1

print(result)