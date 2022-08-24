'''
1은 집이 있는 곳
0은 집이 없는곳
입력)
- N 정사각형 [5\25]
'''

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
_board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
ans = []
cnt = 0

def valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N


def dfs(r, c, cnt):
    visited[r][c] = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if valid_coord(nr, nc):
            if not visited[nr][nc] and _board[nr][nc]:
                cnt = dfs(nr, nc, cnt+1)
    return cnt

for r in range(N):
    for c in range(N):
        if not visited[r][c] and _board[r][c]:
            ans.append(dfs(r, c, 1))
            
ans.sort()
print(len(ans))
print(*ans, sep='\n')