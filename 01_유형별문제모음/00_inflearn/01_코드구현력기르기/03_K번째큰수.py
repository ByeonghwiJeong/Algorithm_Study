from itertools import combinations
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
l = list(map(int, input().split()))
r = set()

c = list(combinations(l, 3))
for i in c:
  r.add(sum(i))

r=list(r)
r.sort(reverse=True)
print(r[K-1])
