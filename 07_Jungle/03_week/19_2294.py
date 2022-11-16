from collections import deque
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = set([int(input()) for _ in range(n)])
dp = [0] * (k + 1)


def bfs(x, s):
    q = deque()
    q.append((x, s))
    while q:
        x, s = q.popleft()
        for i in a:
            if s + i > k: continue
            if dp[s + i]: continue
            dp[s + i] = x
            q.append((x + 1, s + i))

bfs(1, 0)
if dp[k]: print(dp[k])
else: print(-1)