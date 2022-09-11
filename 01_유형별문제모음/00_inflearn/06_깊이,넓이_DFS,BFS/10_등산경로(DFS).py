'''
N x N 에 숫자가 있다.
이동시에는 더 높은 구역으로만 이동한다.
'''
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
_board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
dr = (0, 1, 0, -1)
dc = (1, 0 ,-1 ,0)
start = (0, 0)
end = (0, 0)
_min = 987654321
_max = -987654321
for i in range(N):
    for j in range(N):
        v = _board[i][j]
        if v < _min:
            _min = v
            start = (i, j)
        if v > _max:
            _max = v
            end = (i, j)
result = 0

def dfs(sr, sc):
    global result
    if sr == end[0] and sc == end[1]:
        result += 1
    else:
        for i in range(4):
            nr = sr + dr[i]
            nc = sc + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if _board[nr][nc] > _board[sr][sc]:
                          visited[nr][nc] = True
                          dfs(nr, nc)
                          visited[nr][nc] = False

dfs(*start)
print(result)
