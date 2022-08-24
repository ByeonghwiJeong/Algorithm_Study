'''
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10

1  1  1  1  1
1  0  0  1

탐색여부를 -1에서 0으로 바꾸어줘야 시간초과를 막을수 있음
'''
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

M, N = map(int, input().split())
_board = [list(map(int, input().split())) for _ in range(M)]

dp = [[-1] * N for _ in range(M)]
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)
# r행 c열에 몇번 도착했는지 반환
dp[M-1][N-1] = 1

def dfs(r, c):
    # 목적지 도착
    if r == M - 1 and c == N -1:
        return dp[M-1][N-1]
    # 탐색 유무 확인
    if dp[r][c] == -1:
        dp[r][c] = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 2차원배열 범위 확인 & 높이 체크
            if 0 <= nr < M and 0 <= nc < N:
                if _board[r][c] > _board[nr][nc]:
                    dp[r][c] += dfs(nr, nc)
    return dp[r][c]

# M 세로 N 가로
print(dfs(0, 0))

