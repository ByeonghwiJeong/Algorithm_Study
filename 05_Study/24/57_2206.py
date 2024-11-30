"""
https://www.acmicpc.net/problem/2206

제목: 벽 부수고 이동하기

문제)
- n x m 크기 직사각형
- 
"""
from collections import deque
import sys

input = sys.stdin.readline


n, m = map(int, input().split())
# n : 세로 row, m : 가로 col
dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

graph = [list(map(int, input().strip())) for _ in range(n)]

visited = [[[-1] * m for _ in range(n)] for _ in range(2)]



def bfs():
    q = deque()
    q.append((0, 0, 0))
    visited[0][0][0] = 1

    while q:
        r, c, w = q.popleft()
        if r == n-1 and c == m-1:
            return visited[w][r][c]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if not (0 <= nr < n and 0 <= nc < m):
                continue
            if visited[w][nr][nc] != -1:
                continue
            if graph[nr][nc] == 0: # 이동가능 & 방문하지 않은 경우
                visited[w][nr][nc] = visited[w][r][c] + 1
                q.append((nr, nc, w))
            if graph[nr][nc] == 1 and w == 0: # 벽이 있고, 벽을 부술수 있는 경우  & 방문하지 않은 경우
                visited[1][nr][nc] = visited[w][r][c] + 1
                q.append((nr, nc, 1))
    return -1


result = bfs()
print(result)
