import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
r = int(input())

def dfs(r, tree):
    tree[r] = -2
    for i in range(n):
        if tree[i] == n:
            dfs(i, tree)

dfs(r, a)
count = 0
for i in range(n):
    if a[i]!=-2 and i not in a:
        count += 1
print(count)