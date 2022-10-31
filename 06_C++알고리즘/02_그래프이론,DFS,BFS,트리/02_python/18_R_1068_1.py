import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
adj = [[] for _ in range(n)]
r = int(input())

def dfs(now):
    ret = 0
    child = 0
    for next in adj[now]:
        if next == r: continue
        ret += dfs(next)
        child += 1;
    if child == 0: return 1
    return ret

for i, v in enumerate(a):
    if v == -1: root = i
    else: adj[v].append(i)
if r == root: print(0)
else: print(dfs(root))