'''
R과 G의 차이를 못느낌
N x N 에서 RGB로 구성


'''
import sys
sys.setrecursionlimit(10 ** 7)

N = int(input())
_board = [list(input().rstrip()) for _ in range(N)] # R / G / B
_bool = [[True] * N for _ in range(N)] # RG / B
_check1 = [[True] * N for _ in range(N)] # _board 방문체크
_check2 = [[True] * N for _ in range(N)] # _bool 방문체크

# RG >>  True // B >> False
for i in range(N):
    for j in range(N):
        if _board[i][j] == 'B':
            _bool[i][j] = False

# 방향벡터
dr = (0, 1, 0, -1)
dc = (1, 0, -1, 0)

# 좌표계 안에 있는지
def coord_vaild(r, c):
    return 0<= r < N and 0 <= c < N

def dfs(r, c, a):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if a == _board: # 첫번째 경우 체크 R / G / B
            if coord_vaild(nr, nc) and a[nr][nc] == a[r][c] and _check1[nr][nc]:
                _check1[nr][nc] = False
                dfs(nr, nc, a) 
        elif a == _bool: # 두번째 경우 체크 RG / B
            if coord_vaild(nr, nc) and a[nr][nc] == a[r][c] and _check2[nr][nc]:
                _check2[nr][nc] = False
                dfs(nr, nc, a) 
    return


a = 0
b = 0
for i in range(N):
    for j in range(N):
        if _check1[i][j]: # 첫번째 R / G / B
            a += 1
            _check1[i][j] = False
            dfs(i, j, _board)
        if _check2[i][j]: # 두번째  RG / B
            b += 1
            _check2[i][j] = False
            dfs(i, j, _bool)

print(a, b)