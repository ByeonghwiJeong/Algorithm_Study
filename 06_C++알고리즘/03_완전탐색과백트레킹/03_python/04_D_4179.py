'''
<불!>
https://www.acmicpc.net/problem/4179
문제 : BFS)
- 지훈이와 불은 매 분마다 4방향이동
- 불과 벽이있는 공간 이동 x
- 지훈이가 불에 타기전에 탈출할 수 있는지 구하라
입력)
- R x C 크기의 미로, 1 <= R, C <= 1000
    - # : 벽
    - . : 빈칸
    - J : 지훈이의 위치
    - F : 불의 위치
출력)
- 탈출 불가능 : IMPOSSIBLE
- 지훈이가 미로를 탈출하는데 걸리는 최소시간
'''
from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
a = [list(input().rstrip()) for _ in range(R)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
q = deque()
INF = int(1e9)
fire_check = [[INF] * C for _ in range(R)]
jihun_check = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if a[i][j] == 'F':
            q.append((i, j))
            fire_check[i][j] = 1
        elif a[i][j] == 'J':
            sr = i
            sc = j

while q:
    r, c = q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if not fire_check[nr][nc] == INF: continue
            if a[nr][nc] == '#': continue
            fire_check[nr][nc] = fire_check[r][c] + 1
            q.append((nr, nc))

jihun_check[sr][sc] = 1
q.append((sr, sc))
ret = 0
while q:
    r, c = q.popleft()
    if r == 0 or r == R-1 or c == 0 or c == C-1:
        # print(jihun_check[r][c])
        # exit(0)
        ret = jihun_check[r][c]
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if not jihun_check[nr][nc] == 0: continue
            if a[nr][nc] == '#': continue
            if jihun_check[nr][nc] != 0: continue
            if jihun_check[r][c] + 1 >= fire_check[nr][nc]: continue
            jihun_check[nr][nc] = jihun_check[r][c] + 1
            q.append((nr, nc))
if ret: print(ret)
else: print('IMPOSSIBLE')

'''
- 불 체크 배열에서 불이 없는경우의 반례를 대비해서 INF로 초기화
- 가장자리에 도달한경우 break!!!!
'''