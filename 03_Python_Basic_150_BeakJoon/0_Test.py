import sys
input = sys.stdin.readline

from itertools import combinations

l = []
for _ in range(9):
    l.append(int(input()))

S = combinations(l, 7)
for s in S:
    if sum(s) == 100:
        print(*s, sep='\n')
