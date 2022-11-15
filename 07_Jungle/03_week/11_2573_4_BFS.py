'''
< 빙산 > 
https://www.acmicpc.net/problem/2573
문제) 
- 2차원 배열에 빙산 높이가 주어진다.
    - 바다인경우 0
- 1년마다 그 칸에 동서남북 네 방향으로 \
    붙어있는 0이 저장된 칸의 개수 만큼 줄어든다. 
- 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하라
- 다 녹을때까지 두덩어리 이상 분리 안되면 0출력
입력)
- 1     : 
출력)
- 1     : 
'''
from collections import deque
import sys
sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n, m = map(int, input().split())
visited = [[0] * m for _ in range(n)]
a = [list(map(int, input().split())) for _ in range(n)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
cnt = 0

def bfs1(r, c): # Count compo
    global visited
    visited[r][c] = 1
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if visited[nr][nc]: continue
                if not a[nr][nc]: # 지우기
                    ice[r][c] += 1
                else:
                    visited[nr][nc] = 1
                    q.append((nr, nc))


while True:
    visited = [[0] * m for _ in range(n)]
    ice = [[0] * m for _ in range(n)]
    compo = 0
    for i in range(n): # 컴포넌트 개수
        for j in range(m):
            if visited[i][j]: continue
            if not a[i][j]: continue # 0인경우 pass
            bfs1(i, j)
            compo += 1

    if compo == 0:
        print(0)
        break
    if compo >= 2:
        print(cnt)
        break

    cnt += 1

    for i in range(n):
        for j in range(m):
            if ice[i][j]:
                a[i][j] -= ice[i][j]
            if a[i][j] < 0: a[i][j] = 0
'''

'''