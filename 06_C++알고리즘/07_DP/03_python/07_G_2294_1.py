'''
https://www.acmicpc.net/problem/2294
문제 : 동전 2

- n가지 종류 동전
- 동전을 조합해서 k원을 만들려고 한다.
- 동전의 최소 개수를 구하라.
- 가치가 같은 동전이 여러 번 주어질 수도 있다

입력)
- 1 : n ~ [1, 100], k ~ [1, 10000]
- 2 ~ n+1 : 각 동전의 가치
'''
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