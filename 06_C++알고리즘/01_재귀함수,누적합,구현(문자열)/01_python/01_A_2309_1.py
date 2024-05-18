import sys
from itertools import combinations
input = sys.stdin.readline

m = [int(input()) for _ in range(9)]
m.sort()
s = sum(m)

for i in combinations(m, 2):
    if s - sum(i) == 100:
        for j in m:
            if j in {i[0], i[1]}: continue
            print(j)
        sys.exit()
