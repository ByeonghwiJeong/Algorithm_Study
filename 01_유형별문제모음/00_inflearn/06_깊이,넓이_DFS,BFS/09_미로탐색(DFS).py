'''
7 x 7 격자판에서 경로의 경로수를 출력하는 프로그램
1은 벽 0은 통로이다.
입력)
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0
출력)
8
'''
import sys
sys.setrecursionlimit(10 ** 7)

_board = [list(map(int, input().split())) for _ in range(7)]
visited = [[False] * 7 for _ in range(7)]

dc = (1, 0, -1, 0)
dr = (0, 1, 0, -1)

result = 0

def dfs(r, c):
    global result
    if r == 6 and c == 6:
        result += 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 7 and 0 <= nc < 7:
            if not visited[nr][nc]:
                if not _board[nr][nc]: # 0이면(통로)
                    visited[nr][nc] = True
                    dfs(nr, nc)
                    visited[nr][nc] = False

visited[0][0] = True
dfs(0, 0)
print(result)