'''
< 벽 부수고 이동하기 >
https://www.acmicpc.net/problem/2206
문제)
- N x M 
    - 1 : 벽
    - 0 : 이동가능
- (1, 1)에서 (N, M)의 위치까지 이동하려 한다.
- 경로가 짧아진다면 벽을 한개 부수고 이동하여도 된다.
'''
import sys
sys.setrecursionlimit(10 ** 6)
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

def bfs():
    global visited
    q = deque()
    q.append((0, 0, 1)) # r, c, 벽
    visited[0][0][0] = 1
    while q:
        r, c, w = q.popleft()
        if r == n - 1 and c == m - 1: return max(visited[n - 1][m - 1])
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < n and 0 <= nc < m:
                if a[nr][nc]: # Next대상 벽 (1)
                    if not w: continue
                    if visited[nr][nc][1]: continue
                    q.append((nr, nc, 0))
                    visited[nr][nc][1] = visited[r][c][0] + 1
                else: # Next대상 벽X (0)
                    if w: # 벽안부심
                        if visited[nr][nc][0]: continue
                        q.append((nr, nc, 1))
                        visited[nr][nc][0] = visited[r][c][0] + 1
                    else: # 벽부심
                        if visited[nr][nc][1]: continue
                        q.append((nr, nc, 0))
                        visited[nr][nc][1] = visited[r][c][1] + 1
    return -1

print(bfs())
