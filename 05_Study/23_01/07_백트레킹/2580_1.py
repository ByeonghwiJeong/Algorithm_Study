'''
행, 열, 3x3 : 1 ~ 9가 존재하는지 체크
check_row[i][j] = i행에 j존재?
check_col[i][j] = i열에 j존재?
check_3x3[i][j]
    (row, col)
    - (0, 0) (0, 1) (0, 2)
    - (1, 0) (1, 1) (1, 2)
    - (2, 0) (2, 1) (2, 2)
    -> 0 ~ 8 구간


'''

import sys
input = sys.stdin.readline
sudoku = [list(map(int, input().split())) for _ in range(9)]
