'''
< 탈출 > 
https://www.acmicpc.net/problem/3055
문제) 
- 지도는 R행 C열
- 홍수가 나서 고슴도치는 친구 비버굴로 도망간다.
- 비어있는곳 '.' \ 물이차있는곳 '*' \ 돌은 'x'
- 비버의 굴 'D' \ 고슴도치의 위치 'S'
- 매분마다 상하좌우이동
- 물도 매분마다 인접한 비어있는 칸으로 확장
입력)
- 1     : R, C
출력)
- 
'''
from collections import deque
import sys
input = sys.stdin.readline

dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

R, C = map(int, input().split())
a = [list(input().rstrip()) for _ in range(R)]
w = []
for i in range(R):
    for j in range(C):
        if a[i][j] == 'S': start = (i, j)
        if a[i][j] == '*': w.append((i, j))

q = deque([start])
wq = deque(w)
ret = 0
while q:
    for _ in range(len(wq)):
        r, c = wq.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if a[nr][nc] == '.': # S부분 탐색은 할필요없음
                    a[nr][nc] = '*'
                    wq.append((nr, nc))
    for _ in range(len(q)):
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if a[nr][nc] == 'D': print(ret + 1); exit(0)
                if not a[nr][nc] == '.': continue
                a[nr][nc] = 'S'
                q.append((nr, nc))
    for i in a:
        print(i)
    ret += 1
print('KAKTUS')
