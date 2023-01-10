'''
스도쿠

'''
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

# 빈칸 
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j]: continue
        blank.append((i, j))

# value check
def val_check(r, c, v):
    row = r // 3 * 3
    col = c // 3 * 3
    for i in range(9):
        # row
        if board[r][i] == v: return False
        # col
        if board[i][c] == v: return False

    for i in range(row, row + 3):
        for j in range(col, col + 3):
            if board[i][j] == v: return False
    
    return True
        # 3 x 3

# dfs n : 처리한 빈칸수
def dfs(n):
    if n == len(blank):
        pass
        return
    r, c = blank[n]
    for i in range(1, 10):
        if val_check(r, c, i):
            board[r][c] = i
            dfs(n + 1)
            board[r][c] = 0

dfs(0)