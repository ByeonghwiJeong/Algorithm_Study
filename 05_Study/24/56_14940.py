"""
https://www.acmicpc.net/problem/14940
제목: 쉬운 최단거리

문제)
- 0 : 이동 X
- 1 : 이동 O
- 2 : 목표지점

"""
from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
# n : 세로, m : 가로

graph = [list(map(int, input().split())) for _ in range(n)]
# 목쵸지점 찾기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            goal = (i, j)
            break

visited = [[0] * m for _ in range(n)]

dr = (-1, 0, 1, 0)
dc = (0, -1, 0, 1)

# (0, 0)에서 시작
def bfs():
    q = deque([goal])
    visited[goal[0]][goal[1]] = 0


    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc] == 0 and graph[nr][nc] == 1:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))

bfs()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = -1

    print(*visited[i])