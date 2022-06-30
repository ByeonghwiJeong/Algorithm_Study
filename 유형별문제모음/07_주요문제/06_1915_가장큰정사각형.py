'''
1 <= n m <= 1000

완전탐색기준 불가능

1x1 >> n x m
2x2 >> n-1 x m-1
3x3 >> n-2 x m-2
4x4 >> n-3 x m-3
.
.
.
1000x1000
>>> sigma i^2 i=1 ... 1000
3억 >> 시간초과 

[[ 동적계획법 ]]
[[ bottom-Up방식풀이 ]] 

'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# arr = [list(input().strip()) for _ in range(n)]
arr = [input().strip() for _ in range(n)]
dp = [[0] * m for _ in range(n)]

for j in range(m):
    if arr[0][j] == '1':
        dp[0][j] = 1

for i in range(1, n):
    if arr[i][0] == '1':
        dp[i][0] = 1
    for j in range(1, m):
        if arr[i][j] == '1':
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans**2)