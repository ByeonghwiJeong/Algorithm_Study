'''
토마토 visited 없이 토마토 상자에 일수체크하기
'''
from collections import deque
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1, 0, 0)
dc = (1, 0, -1, 0, 0, 0)
dl = (0, 0, 0, 0, 1, -1)

m, n, h = map(int, input().split()) # c, r, h
a = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
t = []
ans = -1
for k in range(h): # l
    for i in range(n): # r
        for j in range(m): # c
            if a[k][i][j] == 1: 
                t.append((k, i, j)) # d, l, r, c


def bfs():
    global t
    q = deque(t)
    while q:
        l, r, c = q.popleft()
        for i in range(6):
            nr = r + dr[i]
            nc = c + dc[i]
            nl = l + dl[i]
            if 0 <= nr < n and 0 <= nc < m and 0 <= nl < h:
                if a[nl][nr][nc]: continue # 1익은 -1없음 pass
                a[nl][nr][nc] = a[l][r][c] + 1
                q.append((nl, nr, nc))

bfs()
ans = 0
for i in a:
    for j in i:
        for k in j:
            if k == 0: print(-1); exit(0)
        ans = max(ans, max(j))
                
print(ans - 1)

