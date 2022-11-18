'''
< 장난감 조립 > 
https://www.acmicpc.net/problem/2637
문제) 
- 우리는 어떤 장난감을 여러 부품으로 조립하려한다.
- 장난감 = 기본부품 + 중간 부품
- 기본 부품은 더 이상 쪼개질수 없음
입력)
- 1     : N ~ [3 \ 100]
- 2     : M ~ [3 \ 100]
- 3[M]  : X, Y, K
    - X를 만드는데 Y가 K개 필요함
출력)
- 
'''
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
l = [list(map(int, input().split())) for _ in range(m)]
l.sort() # 
dp = [[0] * (n + 1) for _ in range(n + 1)]
for x, y, k in l:
    dp[x][0] = 1
    if dp[y][0]: 
        for i in range(1, n + 1):
            if dp[y][i]: dp[x][i] += dp[y][i] * k
    else:
        dp[x][y] = k

for i, v in enumerate(dp[n][1:]):
    if v > 0: print(i + 1, v)