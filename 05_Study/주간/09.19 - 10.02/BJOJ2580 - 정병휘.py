"""
< 스도쿠 >
https://www.acmicpc.net/problem/2580
"""
import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
# 빈칸체크
blank = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            blank.append((i, j))

def valid_value(r, c, v):
    row = r // 3 * 3
    col = c // 3 * 3
    for i in range(9): # 0 ~ 8 
    # i // 3 :  0 0 0 1 1 1 2 2 2
    # i %  3 :  0 1 2 0 1 2 0 1 2
        # row
        if board[r][i] == v:
            return False
        # col
        if board[i][c] == v:
            return False
        # rec
        if board[row + i // 3][col + i % 3] == v:
            return False
    return True

def dfs(n):
    if n == len(blank):
        for i in board:
            print(*i)
        sys.exit(0)
    r = blank[n][0]
    c = blank[n][1]
    for i in range(1, 10):
        if valid_value(r, c, i):
            board[r][c] = i
            dfs(n + 1)
            board[r][c] = 0
dfs(0)
'''
1. 빈칸 부분의 좌표를 먼저 저장했다.
2. dfs의 매개변수를 빈칸을 채우는 갯수로 해서 빈칸수와 일치했을때 print & exit 
3. 특정위치에 rec부분을 탐색하기위에서 0 ~ 8 숫자의 3에대한 몫과 나머지를 활용했다
'''