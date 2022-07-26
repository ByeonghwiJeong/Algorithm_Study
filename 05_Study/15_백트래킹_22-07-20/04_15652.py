import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
rs = []

def recur(n):
    if len(rs) == M:
        print(*rs, sep=' ')
        return
    for i in range(n, N + 1):
        rs.append(i)
        recur(i)
        rs.pop()

recur(1)