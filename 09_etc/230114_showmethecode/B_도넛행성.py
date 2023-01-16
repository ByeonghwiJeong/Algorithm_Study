'''
< 도넛행성 >
문제)
- 준겸이는 N x M칸으로 이루어진 도넛 모양의 행성에 살고 있다.
- 상하좌우 이동
- 비어있는칸 : 0, 벽 : 1
'''
from collections import deque
import sys
input = sys.stdin.readline

dr = (-1, 1, 0, 0)
dc = (0, 0, -1, 1)

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def go(r, c):
    visited[r][c] = True
    q = deque()
    q.append((r, c))
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = (r + dr[i]) % N
            nc = (c + dc[i]) % M 
            if a[nr][nc] == 1: continue
            if visited[nr][nc]: continue
            visited[nr][nc] = True
            q.append((nr, nc))
            
cnt = 0
for i in range(N):
    for j in range(M):
        if a[i][j] == 1: continue # 벽 pass
        if visited[i][j]: continue # 이미 방문한 곳 pass
        go(i, j)
        cnt += 1
print(cnt)