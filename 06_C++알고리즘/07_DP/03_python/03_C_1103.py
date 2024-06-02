"""
https://www.acmicpc.net/problem/1103
백준 1103. 게임, G2
- 1 ~ 9 숫자, 구멍이 있는 보드
- 보드 가장 왼쪽위에 동전이 놓여있음
    1. 동전이 있는 칸에 쓰여 있는 숫자 X
    2. 동전을 위, 아래, 왼쪽, 오른쪽으로 움직일 수 있음
    3. 위에서 고른 방향으로 X칸 이동 (중간 구멍 무시)
- 구멍에 빠지면 게임 종료
- 보드 밖으로 나가면 게임 종료
- 최대 몇 번 움직일 수 있는지 구하기
- 동전을 무한히 움직일 수 있다면 -1 출력

"""

# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]

# def in_range(y, x):
#     return 1 <= y <= t and 1 <= x <= a

# def down(y, x):
#     if not in_range(y, x) or b[y][x] == 'H':
#         return 0
#     if check[y][x]:
#         print(-1)
#         exit(0)
#     if d[y][x]:
#         return d[y][x]

#     check[y][x] = 1
#     value = int(b[y][x])
#     for i in range(4):
#         ny = y + dy[i] * value
#         nx = x + dx[i] * value
#         d[y][x] = max(d[y][x], down(ny, nx) + 1)
#     check[y][x] = 0
#     return d[y][x]

# t, a = map(int, input().split())
# b = [[0 for _ in range(a + 1)] for _ in range(t + 1)]
# d = [[0 for _ in range(a + 1)] for _ in range(t + 1)]
# check = [[0 for _ in range(a + 1)] for _ in range(t + 1)]

# for i in range(1, t + 1):
#     s = input().strip()
#     for j in range(1, a + 1):
#         b[i][j] = s[j - 1]

# print(down(1, 1))

import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dp = [[0] * M for _ in range(N)]


result = 0

def dfs(r, c, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nr = r + dr[i] * int(board[r][c])
        nc = c + dc[i] * int(board[r][c])
        if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != 'H' and cnt + 1 > dp[nr][nc]:
        # 보드 경계 IN
        # 구멍이 아닌 경우
        # 최대 이동 횟수 갱신
            if visited[nr][nc] == 1:
                print(-1)
                exit(0)
            else:
                dp[nr][nc] = cnt + 1
                visited[nr][nc] = 1
                dfs(nr, nc, cnt + 1)
                visited[nr][nc] = 0

dfs(0, 0, 1)
print(result)