'''
대각선 / (positive diag)
    -> r + c 일정
대각선 \ (negative diag)
    -> r - c 일정
'''
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def backtrack(r):
    global res
    if r == N:
        res += 1
        return
    # c : col , r : row
    for c in range(N):
        if c in col or (r + c) in posDiag  or (r - c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)

        backtrack(r + 1)

        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)


N = int(input())
col = set()
posDiag = set()
negDiag = set()
res = 0

backtrack(0)
print(res)