"""
< 미로 탐색 >
https://www.acmicpc.net/problem/2178
문제
- N x M 배열에서 1:이동가능 / 0:이동불가
- (1, 1)에서 출발하여 (N, M)의 위치로 이동
- 지나야하는 최소 칸수
- N, M ~ [2 \ 100]
입력
4 6
101111
101010
101011
111011
출력
15
"""
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())
_board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def valid_coord(r, c):
    return 0<=r<N and 0<=c<M

def bfs():
    visited[0][0] = 1
    q = deque()
    q.append((0, 0))
    while q:
        r, c = q.popleft()
        if r == N - 1 and c == M - 1:
            return visited[r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not valid_coord(nr, nc): continue
            if visited[nr][nc]: continue
            if not _board[nr][nc]: continue
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))

print(bfs())