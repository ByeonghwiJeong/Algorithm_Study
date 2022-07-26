import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
#  1, 1 / 2, 4
N = int(input())
board = [[True] * (N + 1) for _ in range(N + 1)]
# 1 ~ N x 1 ~ N 체스판
'''

'''
dx = (1, -1, 1, -1)
dy = (1, -1, -1, 1)

def is_valid_coord(y, x):
    return 1<= y <= N and 1<= x <= N

def paint_board(y, x, chk):
    board[y][x] = chk
    for i in range(4):
        tmp_y = y
        tmp_x = x
        while is_valid_coord(tmp_y, tmp_x):
            print(y, x, tmp_y, tmp_x)
            board[tmp_y][tmp_x] = chk
            tmp_y += dy[i]
            tmp_x += dx[i]

def recur(n):
    if n == N:
        global cnt
        cnt += 1
        return
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if board[i][j] == True:
                paint_board(i, j, False)
                recur(n + 1)
                paint_board(i, j, True) # rollback

cnt = 0
recur(0)
print(cnt)
