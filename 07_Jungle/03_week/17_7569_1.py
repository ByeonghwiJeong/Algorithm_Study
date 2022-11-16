'''
< 토마토 > 
https://www.acmicpc.net/problem/7569
문제) 
- 높이H, 세로N, 가로M
- 익은 토마토에 인접한 익지 않은 토마토들이 영향을 받아 익는다.
- 몇일 뒤에 토마토들이 다 익게 되는지 최소 일수
- 빈칸, 익은토마토, 익지않은토마토
입력)
- 1     : 상자의 가로 칸 M, 상자의 세로칸 N, 상자수 H 
        - M ~ [2 \ 100], N ~ [2 \ 100], H ~ [1 \ 100]
- 2[NxH]: 익은 1, 익지않은 0, 토마토없는경우 -1
출력)
- 모두 익을 때까지 걸리는 일수
    - 초기에 모두 익어있으면 0
    - 모두 익지 못하면 -1
'''
from collections import deque
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1, 0, 0)
dc = (1, 0, -1, 0, 0, 0)
dl = (0, 0, 0, 0, 1, -1)

m, n, h = map(int, input().split()) # c, r, h
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
visited = [[[0] * m for _ in range(n)] for _ in range(h)]
t = []
ans = -1
for k in range(h): # l
    for i in range(n): # r
        for j in range(m): # c
            if a[k][i][j] == 1: 
                t.append((0, k, i, j)) # d, l, r, c
                visited[k][i][j] = 1


def bfs():
    global t, ans
    q = deque(t)
    while q:
        d, l, r, c = q.popleft()
        ans = max(ans, d)
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nl = l + dl[i]
            if 0 <= nr < n and 0 <= nc < m and 0 <= nl < h:
                if visited[nl][nr][nc]: continue
                if a[nl][nr][nc]: continue # 1익은 -1없음 pass
                a[nl][nr][nc] = 1
                visited[nl][nr][nc] = 1
                q.append((d + 1, nl, nr, nc))

bfs()
flag = True
for k in range(h):
    for i in range(n):
        for j in range(m):
            # if a[k][i][j] == 0: flag = False
            if a[k][i][j] == 0: print(-1); exit(0)
                
print(ans)

