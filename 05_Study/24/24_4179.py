'''
https://www.acmicpc.net/problem/4179
제목 : 불!

문제)
- 지훈이는 미로에서 일하고 탈출하도록 도와주자
- 미로에서 지훈이의 위치와 불이 붙은 위치를 감ㅇ란해서 지훈이가 불에 타기전에 탈출할 수 있는지의 여부
- 얼마나 빨리 탈출할 수 있는지를 결정
- 지훈이와 불은 매분마다 한칸씩 수평 또는 수직으로 이동
- 불은 각지점에서 네방향으로 확산
- 미로의 가장자리에 접한 공간에서 탈출 할 수 있음
- 지훈이와 불은 벽이 있는 공간은 통과하지 못함
    - # : 벽
    - . : 지나갈수 있는공간
    - J : 미로에서의 초기위치 
    - F : 불이 난 공간

입력 예시)
4 4
####
#JF#
#..#
#..#

'''
from collections import deque
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

R, C = map(int, input().split())
a = [list(input().rstrip()) for _ in range(R)]

fire_q = deque()
jihun_q = deque()
INF = int(1e9)
fire_check = [[INF] * C for _ in range(R)]
jihun_check = [[0] * C for _ in range(R)]
sr, sc = -1, -1  # 지훈이 위치 저장 변수


# initial
for i in range(R):
    for j in range(C):
        if a[i][j] == 'F':  # 불이 난 위치
            fire_q.append((i, j))
            fire_check[i][j] = 1
        elif a[i][j] == 'J':  # 지훈이 위치
            sr, sc = i, j
            jihun_q.append((i, j))
            jihun_check[i][j] = 1

# 미리 지훈이가 가장자리에 있는 경우 체크
if sr == 0 or sr == R-1 or sc == 0 or sc == C-1:
    print(1)
    exit()

# 불의 확산 BFS
while fire_q:
    r, c = fire_q.popleft()
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if fire_check[nr][nc] != INF: continue # 방문했음
            if a[nr][nc] == '#': continue # 벽인 경우
            fire_check[nr][nc] = fire_check[r][c] + 1
            fire_q.append((nr, nc))


# 지훈이의 이동 BFS
jihun_check[sr][sc] = 1

while jihun_q:
    r, c = jihun_q.popleft()

    # 미로 가장자리 탈출 성공
    if r == 0 or r == R-1 or c == 0 or c == C-1:
        print(jihun_check[r][c])
        exit()

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C:
            if jihun_check[nr][nc] != 0: continue # 이미 방문
            if a[nr][nc] == '#': continue # 벽인 경우
            if jihun_check[r][c] + 1 >= fire_check[nr][nc]: continue
            # 불이 먼저 도착
            jihun_check[nr][nc] = jihun_check[r][c] + 1
            jihun_q.append((nr, nc))

print("IMPOSSIBLE")


