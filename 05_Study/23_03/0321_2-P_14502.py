'''
< 연구소 >
https://www.acmicpc.net/problem/14502
문제)
- 바이러스 확산 방지를 위해서 벽을 세우려고 한다.
- 크기 N x M 직사각형, 0은 빈칸, 2는 바이러스가 있는 곳
- 바이러스는 상하좌우로 전염
- 세울 수 있는 벽의 개수는 3개이다.
- 벽을 3개 세운 뒤, 바이러스가 퍼질수 없는 곳을 안전영역이라고한다.
- 안전 영역 크기의 최댓값

입력)
- 1     : 세로크기N, 가로크기M
- 2[N]  : N개의 줄에 지도의 모양이 주어진다.
출력)
- 1     : 안정영역의 최대 크기
'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)] 
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def dfs(r, c):
    global visited
    if a[r][c] == 1 or visited[r][c]: return
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            dfs(nr, nc)

def solve():
    global visited
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if a[i][j] == 2: dfs(i, j)
    ret = 0
    for i in range(N):
        for j in range(M):
            if a[i][j] == 0 and visited[i][j] == 0:
                ret += 1
    return ret 

b = []
for i in range(N):
    for j in range(M):
        if not a[i][j]: b.append((i, j))
ans = 0
for i in range(len(b)):
    for j in range(i):
        for k in range(j):
            a[b[i][0]][b[i][1]] = 1
            a[b[j][0]][b[j][1]] = 1
            a[b[k][0]][b[k][1]] = 1
            ans = max(ans, solve())
            a[b[i][0]][b[i][1]] = 0
            a[b[j][0]][b[j][1]] = 0
            a[b[k][0]][b[k][1]] = 0
print(ans)