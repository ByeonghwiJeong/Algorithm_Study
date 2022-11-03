from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
_h = []
_c = []
for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if v == 1: _h.append((i, j))
        if v == 2: _c.append((i, j))
def dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

ans = 987654321
for combi in combinations(_c, m):
    tot = 0
    for h in _h:
        tot += min(dist(h, c) for c in combi)
    ans = min(ans, tot)
print(ans)

