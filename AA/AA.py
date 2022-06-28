import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
store = []
home = []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            store.append((i, j))
        if city[i][j] == 2:
            home.append((i, j))

ans = float('inf')
for ss in combinations(store, M):
    tot = 0
    for h in home:
        mindis = float('inf')
        for s in ss:
            mindis = min(mindis, abs(s[0]-h[0])+abs(s[1]-h[1]))
        tot += mindis
    ans = min(ans, tot)
print(ans)