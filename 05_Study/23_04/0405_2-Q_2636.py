'''
< 치즈 >
https://www.acmicpc.net/problem/2636
문제)
- 세로n 가로m 최대길이 100 사격형판
- 0:판 / 1:치즈 
- 1시간마다 가장자리부터 녹음
- 다녹기 1시간 직전의 1의 갯수
입력
13 12
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 0
0 1 1 1 0 0 0 1 1 0 0 0
0 1 1 1 1 1 1 0 0 0 0 0
0 1 1 1 1 1 0 1 1 0 0 0
0 1 1 1 1 0 0 1 1 0 0 0
0 0 1 1 0 0 0 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 1 1 1 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
출력
3 - 모두녹는시간
5 - 모두녹기 한 시간 전에 남아있는 치즈 조각
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
cnt = 0

def dfs(r, c):
    global visited, l
    visited[r][c] = 1
    if a[r][c]:
        l.append((r, c))
        return
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc]: continue
            dfs(nr, nc)
    return

while True:
    cnt2 = 0 # 직전 치즈 갯수
    visited = [[0] * M for _ in range(N)]
    l = []
    dfs(0, 0)
    for i in l:
        cnt2 += 1
        a[i[0]][i[1]] = 0
    flag = 0
    for i in range(N):
        for j in range(M):
            if a[i][j]: flag = 1
    cnt += 1 # 전체 시간
    if not flag: break # 1이 하나도없을때 break
print(cnt)
print(cnt2)
