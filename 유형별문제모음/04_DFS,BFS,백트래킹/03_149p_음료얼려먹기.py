'''
connected component 찾기
'''

N, M = map(int, input().split())
list = [list(map(int, input())) for _ in range(N)]
chk = [[False] * M for _ in range(N)]

dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)

def is_valid_coord(y, x):
    return 0<=y<N and 0<=x<M

def is_valid_visit(y, x):
    return list[y][x] == 0 and chk[y][x] == False

def dfs(y, x):
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_valid_coord(ny, nx) and is_valid_visit(ny, nx):
            chk[ny][nx] = True
            dfs(ny, nx)
    return True


cnt = 0

for i in range(N):
    for j in range(M):
        if is_valid_visit(i, j):
            chk[i][j] == True
            if dfs(i, j):
                cnt += 1
print(cnt)