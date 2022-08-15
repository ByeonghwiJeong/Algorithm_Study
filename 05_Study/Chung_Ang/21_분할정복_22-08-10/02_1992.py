import sys
input = sys.stdin.readline

def chk(r1, c1, r2, c2):
    global _board
    for i in range(r1, r2):
        for j in range(c1, c2):
            if _board[i][j] != _board[r1][c1]:
                return False
    return True

def recur(r1, c1, r2, c2):
    global _board
    if chk(r1, c1, r2, c2):
        return str(_board[r1][c1])
    else:
        mr = (r1 + r2) // 2
        mc = (c1 + c2) // 2
        ans = recur(r1, c1, mr, mc) + recur(r1, mc, mr, c2) + \
            recur(mr, c1, r2, mc) + recur(mr, mc, r2, c2)
        return '(' + ans + ')'

N = int(input())
_board = [list(map(int, input().rstrip())) for _ in range(N)]
print(recur(0, 0, N, N))