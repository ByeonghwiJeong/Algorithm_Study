'''
row // col // rec 체크 함수 선언
    - rec 체크시 2중 for문 [0, 3) 방식과 1중 for문 [0, 9) 방식이 있음
    - [0, 9)  >>>  i // 3  , i % 3  >>> 0 0 / 0 1 / 0 2 // 1 0 / 1 1 ...

sys.setrecursionlimit(10 ** 7)
    - 아무때나 사용하면 메모리 초과 발생 할 수 있음

# for i in range(9):
#     board.append(list(map(int, input().split())))

- 위의 방식을 한줄로 표현
    - board = [list(map(int, input().split())) for _ in range(9)]

if n == len(blank):
    for r in board:
        print(*r)
    # exit(0) 매우매우 중요!!!
    exit(0)

- 

'''
import sys
input = sys.stdin.readline
# < 주의 >
# sys.setrecursionlimit(10 ** 7)

board = [list(map(int, input().split())) for _ in range(9)]
blank = []

# for i in range(9):
#     board.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

# def check_row(r, v):
#     for i in range(9):
#         if v == board[r][i]:
#             return False
#     return True

# def check_col(c, v):
#     for i in range(9):
#         if v == board[i][c]:
#             return False
#     return True

# def check_rec(r, c, v):
#     row = r // 3 * 3
#     col = c // 3 * 3
#     for i in range(3):
#         for j in range(3):
#             if v == board[row + i][col + j]:
#                 return False
#     return True

def check_sudoku(r, c, v):
    row = r // 3 * 3
    col = c // 3 * 3
    for i in range(9):
        #row
        if board[r][i] == v:
            return False
        #col
        if board[i][c] == v:
            return False
        #rec 0 0 / 0 1 / 0 2 // 1 0 / .... 
        if board[row + i // 3][col + i % 3] == v:
            return False
    return True

def dfs(n):
    if n == len(blank):
        for r in board:
            print(*r)
        # exit(0) 매우매우 중요!!!
        exit(0)

    r, c = blank[n]

    for i in range(1, 10):
        # if check_row(r, i) and check_col(c, i) and check_rec(r, c, i):
        if check_sudoku(r, c, i):
            board[r][c] = i
            dfs(n + 1)
            board[r][c] = 0

dfs(0)
