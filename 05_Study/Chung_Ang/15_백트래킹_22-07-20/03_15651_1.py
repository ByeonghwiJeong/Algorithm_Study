import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N, M = map(int, input().split())
rs = []

def recur(n):
    if n == M:
        print(*rs, sep=' ')
        return
    for i in range(1, N + 1):
        rs.append(i)
        recur(n + 1)
        rs.pop()

recur(0)
